from .Utils import Utils

class RSACryptor:
    def __init__(self, input_file: str, output_file: str, key_file: str):
        self.input_file = input_file
        self.output_file = output_file

        with open(key_file, 'r') as key_input_file:
            self.key = int(key_input_file.readline().strip())
            self.n = int(key_input_file.readline().strip())

    def encrypt(self):
        Utils.createFoldersInPath(self.output_file)
        output_file = open(self.output_file, 'w', encoding='utf8')
        with open(self.input_file, 'r') as input_file:
            for line in input_file:
                for char in line:
                    code = Utils.fastModuloPow(ord(char), self.key, self.n)
                    output_file.write(str(code) + '\n')
        output_file.close()
        

    def decrypt(self):
        Utils.createFoldersInPath(self.output_file)
        output_file = open(self.output_file, 'w')
        with open(self.input_file, 'r') as input_file:
            for line in input_file:
                code = Utils.fastModuloPow(int(line), self.key, self.n)
                output_file.write(chr(code))
        output_file.close()

