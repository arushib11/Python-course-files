class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __eq__(self,vector):
        if not isinstance(vector,Vector):
            return False
        return self.a==vector.a and self.b==vector.b
    
    def __eq__(self,vector):
        if not isinstance(vector,Vector):
            return False
        return self.a==vector.a and self.b==vector.b
    
    # to return string representation of vector
    def __repr__(self):
        return f"Vector({self.a},{self.b})"

    def __add__(self,vector):
        vector_a=self.a+vector.a
        vector_b=self.b+vector.b
        return Vector(vector_a,vector_b)

    def __sub__(self,vector):
        vector_a=self.a-vector.a
        vector_b=self.b-vector.b
        return Vector(vector_a,vector_b)
    
    def __mul__(self,vector):
        vector_a=self.a*vector.a
        vector_b=self.b*vector.b
        result=vector_a+vector_b
        return result