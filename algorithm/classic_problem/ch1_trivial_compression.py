from sys import getsizeof
import time
from unicodedata import decomposition
    

class CompressedGene(object):
    def __init__(self, gene: str) -> None:
        # self._length = len(gene)
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """Compress gene DNA sequence to bit string
        It save self.bit_string attribute

        A: 0b00, C: 0b01, G: 0b10, T: 0b11

        Examples
        --------
        >>> gene = CompressedGene('ACGTACGTACGT')
        >>> gene.self.bit_string
        >>> 0b000110110001101100011011

        Paramters
        ---------
        gene: str
            gene nucleotide sequence
        
        Returns
        -------
        None
        """
        self.bit_string = 1  ## always start with '1'
        for nuc in gene.upper():
            self.bit_string <<= 2  ## 2 bit 
            if nuc == 'A':
                self.bit_string |= 0b00
            elif nuc == 'C':
                self.bit_string |= 0b01
            elif nuc == 'G':
                self.bit_string |= 0b10
            elif nuc == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError(f'Invalid nucleotide: {nuc}')

    def decompress(self) -> str:
        """Decompress self.bit_string to string"""
        bit_string = self.bit_string
        
        gene = ''
        # while bit_string != 0:
        # for _ in range(self._length):
        for _ in range(0, bit_string.bit_length() - 1, 2):
            nuc_bit = bit_string & 0b11
            if nuc_bit == 0b00:
                gene = 'A' + gene
            elif nuc_bit == 0b01:
                gene = 'C' + gene
            elif nuc_bit == 0b10:
                gene = 'G' + gene
            elif nuc_bit == 0b11:
                gene = 'T' + gene
            else:
                raise ValueError(f'Invalid bit found: {nuc_bit}')
            bit_string >>= 2
        return gene

    def __str__(self) -> str:
        return self.decompress()


class CompressedGeneDict(object):
    def __init__(self, gene: str) -> None:
        # self._length = len(gene)
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """Compress gene DNA sequence to bit string
        It save self.bit_string attribute

        A: 0b00, C: 0b01, G: 0b10, T: 0b11

        Examples
        --------
        >>> gene = CompressedGene('ACGTACGTACGT')
        >>> gene.self.bit_string
        >>> 0b000110110001101100011011

        Paramters
        ---------
        gene: str
            gene nucleotide sequence
        
        Returns
        -------
        None
        """
        
        self.bit_string = 1  ## always start with '1'
        dic_bit = dict([('A', 0b00), ('C', 0b01), ('G', 0b10), ('T', 0b11)])

        for nuc in gene.upper():
            self.bit_string <<= 2  ## 2 bit 
            try:
                self.bit_string |= dic_bit[nuc]
            except KeyError:
                raise ValueError(f'Invalid nucleotide: {nuc}')

    def decompress(self) -> str:
        """Decompress self.bit_string to string"""
        bit_string = self.bit_string
        dic_bit = {0b00: 'A', 0b01: 'C', 0b10: 'G', 0b11: 'T'}
        
        gene = ''
        for _ in range(0, bit_string.bit_length() - 1, 2):
            nuc_bit = bit_string & 0b11
            try:
                gene = dic_bit[nuc_bit] + gene
            except KeyError:
                raise ValueError(f'Invalid bit found: {nuc_bit}')
            bit_string >>= 2
        return gene

    def __str__(self) -> str:
        return self.decompress()

def run_compress():
    
    original = 'TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA' * 100
    print(f'Original: {getsizeof(original)} bytes')
    # compressed = CompressedGene(original)
    compressed = CompressedGeneDict(original)
    # print(f'Compressed: {getsizeof(compressed._length)} bytes')
    print(f'Compressed: {getsizeof(compressed.bit_string)} bytes')
    decompressed = compressed.decompress()
    # print(f'Compressed: {original}')
    # print(f'Decompressed: {decompressed}')
    print(f'Is the same compressed and decompressed {original == decompressed}')
    return

if __name__ == "__main__":    
    run_compress()