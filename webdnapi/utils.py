class Generation:
    def __init__(self, method=None, arguments = None, orig: 'Generation' = None, dictionary=None):
        if orig is not None:
            self.copy(orig)
        elif dictionary is not None:
            self.load(dictionary)
        else:
            self.method: str = method
            self.arguments = []
            self.files = []
            if method == 'generate-sa':
                self.files = ['sequence.txt']
                self.arguments = ['generate-sa.py'] + arguments + self.files
            elif method == 'generate-folded':
                self.files = ['sequence.txt']
                self.arguments = ['generate-folded.py'] + arguments + self.files
            elif method == 'cadnano-interface':
                self.files = ['cadnano-project.json']
                self.arguments = ['cadnano_interface.py'] + self.files + arguments

            if self.files is None:
                raise ValueError('Value of method argument not valid')

    def copy(self, orig: 'Generation'):
        self.method = orig.method
        self.files = orig.files
        self.arguments = orig.arguments

    def load(self, dictionary):
        self.method = dictionary['method']
        self.files = dictionary['files']
        self.arguments = dictionary['arguments']


