using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Task3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private double[] SolveUsingGaussianElimination(double[,] matrix, double[] vector)
        {
            // Реализация метода Гаусса 
            int n = vector.Length;

            // Прямой ход 
            for (int i = 0; i < n; i++)
            {
                // Делим текущую строку на элемент главной диагонали 
                for (int j = i + 1; j < n; j++)
                {
                    double ratio = matrix[j, i] / matrix[i, i];
                    for (int k = i; k < n; k++)
                    {
                        matrix[j, k] -= ratio * matrix[i, k];
                    }
                    vector[j] -= ratio * vector[i];
                }
            }

            // Обратный ход 
            double[] result = new double[n];
            for (int i = n - 1; i >= 0; i--)
            {
                result[i] = vector[i];
                for (int j = i + 1; j < n; j++)
                {
                    result[i] -= matrix[i, j] * result[j];
                }
                result[i] /= matrix[i, i];
            }

            return result;
        }
        static double[] ThomasAlgorithm(double[] a, double[] b, double[] c, double[] f, int n)
        {
            double[] alpha = new double[n]; // Параметры для обратного прогона
            double[] beta = new double[n];

            // Прямой прогон
            alpha[0] = b[0] / a[0];
            beta[0] = f[0] / a[0];

            for (int i = 1; i < n; i++)
            {
                if (i < n - 1)
                    alpha[i] = b[i] / (a[i] - c[i - 1] * alpha[i - 1]);
                beta[i] = (f[i] - c[i - 1] * beta[i - 1]) / (a[i] - c[i - 1] * alpha[i - 1]);
            }

            // Обратный прогон
            double[] x = new double[n];
            x[n - 1] = beta[n - 1];

            for (int i = n - 2; i >= 0; i--)
            {
                x[i] = beta[i] - alpha[i] * x[i + 1];
            }
            Console.WriteLine(alpha[n - 1]);
            return x;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            this.comboBox1.Items.Add("Гаус");
            this.comboBox1.Items.Add("Прогонки");
            this.comboBox1.SelectedText = "Метод";
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string[] matrixLines = textBox1.Text.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries); 
            string[] vectorLines = textBox3.Text.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            int n = Convert.ToInt32(textBox2.Text); double[,] matrix = new double[n, n];
            double[] vector = new double[n];
            // Заполнение матрицы
            for (int i = 0; i < n; i++)
            {
                string[] elements = matrixLines[i].Split(new[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                for (int j = 0; j < n; j++)
                {
                    matrix[i, j] = double.Parse(elements[j]);
                }
            }
            // Заполнение вектора
            for (int i = 0; i < n; i++)
            {
                vector[i] = double.Parse(vectorLines[i]);
            }

            double[] solution;
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                   
                    solution = SolveUsingGaussianElimination(matrix, vector);
                    textBox4.Text = string.Join(", ", solution);
                    break;
                case 1:
                    textBox4.Clear();
                    double[] f = new double[n];
                    for(int i= 0; i < n; i++)
                    {
                        f[i]= double.Parse(vectorLines[i]);
                    }
                    double[]a = new double[n];
                    for(int i = 0; i < n; i++)
                    {
                        a[i]=matrix[i,i];
                    }
                    double[] b = new double[n-1];
                    for(int i = 0; i < n - 1; i++)
                    {
                        b[i] = matrix[i,i+1];
                    }
                    double[]c = new double[n-1];
                    for (int i = 0; i < n - 1; i++)
                    {
                        c[i] = matrix[i+1,i];
                    }
                    double[]x= new double[n];
                    x = ThomasAlgorithm(a, b, c, f,n);
                    textBox4.Text = string.Join(", ", x);
                    break;
            }


        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
