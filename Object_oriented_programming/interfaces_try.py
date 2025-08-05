class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("Must implement compile_code()")
    def execute_code(self):
        raise NotImplementedError("Must implement execute_code()")

class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile GoCode")
    def execute_code(self):
        print("Execute GoCode")

class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Java Code")
    def execute_code(self):
        print("Execute Java Code")    


def run_code(code):
    code.compile_code()
    code.execute_code()

def run_code(code:RunCodeInterface):   # it's accepting any object that implements the RunCodeInterface
    code.compile_code()
    code.execute_code()
    
go=GoCode()
run_code(go)

     
