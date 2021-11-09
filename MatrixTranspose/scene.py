from manim import *
import numpy as np

class ShowMatriz(Scene):
    def construct(self):
        matrix_values = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]
        matrix_values_transposed_empty = [[0] * 3] * 3
        matrix_values_transposed = np.transpose(matrix_values).tolist()
        
        #? add title
        equals = Text('=')
        title = Text('Transpose of a Matrix').scale(1.5).next_to(equals, UP * 10)
        self.play(Write(title))
        
        #? create matrix and put it to the left
        matrix = Matrix(matrix_values)
        self.play(Write(matrix))
        self.play(matrix.animate.shift(LEFT * 3))
        
        #? show '=' at the middle and empty matrix at the right
        matrix_transposed = Matrix(matrix_values_transposed_empty).shift(RIGHT * 3)
        self.play(Write(equals), Write(matrix_transposed.get_brackets()))
        
        matrix_word = MathTex('Matrix A').next_to(matrix, UP)
        matrix_transpose_word = MathTex('Matrix A^T').next_to(matrix_transposed, UP)
        self.play(Write(matrix_word), Write(matrix_transpose_word))
        
        for i in range(len(matrix_values[0])):
            rect_1 = SurroundingRectangle(matrix.copy().get_columns()[i])
            nums_1 = matrix.copy().get_columns()[i]
            group1 = Group(rect_1, nums_1)
            
            matrix_values_transposed_empty[i] = matrix_values_transposed[i]
            matrix_transposed_1 = Matrix(matrix_values_transposed_empty).shift(RIGHT * 3)
            
            self.play(
                Transform(group1, matrix_transposed_1.get_rows()[i]),
                run_time=3
            )
        self.wait(5)
