from triqs_dft_tools.converters import Wannier90Converter
Converter = Wannier90Converter(seedname='nio', bloch_basis=False, rot_mat_type='hloc_diag', add_lambda=None)#,w90zero=2.e-4)
Converter.convert_dft_input()
