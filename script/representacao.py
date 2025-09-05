"""
Módulo para representação molecular e geração de fingerprints.

Este módulo implementa a classe Representacao para conversão de estruturas
moleculares SMILES em representações vetoriais utilizando diferentes algoritmos
de fingerprint molecular.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# RDKit imports
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, PandasTools, Draw, Descriptors, MACCSkeys
from rdkit.Chem import rdFingerprintGenerator
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem.MolStandardize import rdMolStandardize

class Representacao:
    """
    Classe para representação molecular e geração de fingerprints.
    
    Esta classe fornece métodos para converter estruturas moleculares SMILES
    em representações vetoriais utilizando diferentes algoritmos de fingerprint
    molecular, incluindo Morgan e MACCS.
    """

    def __init__(self, dataframe: pd.DataFrame) -> None:
        """
        Inicializa a classe Representacao.
        
        Args:
            dataframe (pd.DataFrame): DataFrame contendo estruturas SMILES
        """
        self.dataframe = dataframe.copy()

    def fingerprint(
        self,
        col_smiles: str,
        fingerprint: str = 'morgan',
        radius: int = 2,
        fp_size: int = 2048,
        use_count: bool = False
    ) -> pd.DataFrame:
        """
        Gera representações vetoriais (fingerprints) das estruturas moleculares.
        
        Args:
            col_smiles (str): Nome da coluna contendo estruturas SMILES
            fingerprint (str): Algoritmo de fingerprint ('morgan' ou 'maccs')
            radius (int): Raio para algoritmo Morgan (padrão: 2)
            fp_size (int): Tamanho do fingerprint (padrão: 2048)
            use_count (bool): Se True, usa contagem de subestruturas (padrão: False)
            
        Returns:
            pd.DataFrame: DataFrame com fingerprints convertidos para arrays
        """
        df = self.mol_to_frame(col_smiles=col_smiles)

        if fingerprint == 'maccs':
            df = self.fp_maccs(col_frames='ROMol')
        else:
            df = self.fp_morgan(
                col_frames='ROMol',
                radius=radius,
                fp_size=fp_size,
                use_count=use_count
            )

        df.dropna(inplace=True)
        df = self.bitvect_to_array('Fingerprint')

        return df
        
    def mol_to_frame(self, col_smiles: str) -> pd.DataFrame:
        """
        Converte estruturas SMILES em objetos moleculares RDKit.
        
        Args:
            col_smiles (str): Nome da coluna contendo estruturas SMILES
            
        Returns:
            pd.DataFrame: DataFrame com coluna ROMol adicionada
        """
        PandasTools.AddMoleculeColumnToFrame(
            frame=self.dataframe,
            smilesCol=col_smiles
        )
        
        return self.dataframe

    def bitvect_to_array(self, col_fp: str) -> pd.DataFrame:
        """
        Converte fingerprints RDKit em arrays NumPy.
        
        Args:
            col_fp (str): Nome da coluna contendo fingerprints RDKit
            
        Returns:
            pd.DataFrame: DataFrame com coluna Features contendo arrays NumPy
        """
        fp_array = []
        
        for index in self.dataframe.index:
            try:
                fp = np.zeros((0,), dtype=np.int8)
                DataStructs.ConvertToNumpyArray(
                    self.dataframe[col_fp][index], fp
                )
            except Exception:
                fp = np.nan

            fp_array.append(fp)
    
        self.dataframe['Features'] = fp_array
    
        return self.dataframe
    
    def fp_maccs(self, col_frames: str) -> pd.DataFrame:
        """
        Gera fingerprints MACCS para as estruturas moleculares.
        
        Args:
            col_frames (str): Nome da coluna contendo objetos moleculares RDKit
            
        Returns:
            pd.DataFrame: DataFrame com coluna Fingerprint contendo MACCS keys
        """
        maccs_lista = []
        
        for index in self.dataframe.index:
            try:
                maccs = MACCSkeys.GenMACCSKeys(
                    self.dataframe[col_frames].iloc[index]
                )
            except Exception:
                maccs = np.nan

            maccs_lista.append(maccs)
    
        self.dataframe['Fingerprint'] = maccs_lista
    
        return self.dataframe
    
    def fp_morgan(
        self,
        col_frames: str,
        radius: int = 2,
        fp_size: int = 2048,
        use_count: bool = False
    ) -> pd.DataFrame:
        """
        Gera fingerprints Morgan para as estruturas moleculares.
        
        Args:
            col_frames (str): Nome da coluna contendo objetos moleculares RDKit
            radius (int): Raio para avaliação de átomos vizinhos (padrão: 2)
            fp_size (int): Tamanho do fingerprint em bits (padrão: 2048)
            use_count (bool): Se True, usa contagem de subestruturas (padrão: False)
            
        Returns:
            pd.DataFrame: DataFrame com coluna Fingerprint contendo Morgan fingerprints
        """
        morgan_lista = []
        
        for index in self.dataframe.index:
            morgan_gen = AllChem.GetMorganGenerator(
                radius=radius, fpSize=fp_size
            )
    
            try:
                if use_count:
                    morgan = morgan_gen.GetCountFingerprint(
                        self.dataframe[col_frames].iloc[index]
                    )
                else:
                    morgan = morgan_gen.GetFingerprint(
                        self.dataframe[col_frames].iloc[index]
                    )
            except Exception:
                morgan = np.nan
                
            morgan_lista.append(morgan)
    
        self.dataframe['Fingerprint'] = morgan_lista
    
        return self.dataframe
    
    