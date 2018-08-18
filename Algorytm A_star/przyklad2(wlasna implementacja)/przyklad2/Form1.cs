using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

// DO UKONCZENIA!!!

namespace przyklad2
{

    public partial class Form1 : Form
    {
        bool pathFound = false;

        bool pickedStart = false;
        bool pickedTarget = false;

        int startX;
        int startY;

        int targetX;
        int targetY;

        PictureBox startingPoint;
        PictureBox targetPoint;

        public int X; 
        public int Y;
        public int F = 0;  // G + H
        public int G = 0;  // score from starting point
        public int H;  // estimated distance

        public Form1()
        {
            InitializeComponent();

            // storing all tiles
            PictureBox[,] matrix = new PictureBox[,]
            {
                { pictureBox1, pictureBox2, pictureBox3, pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9, pictureBox10 },
                { pictureBox20, pictureBox19, pictureBox18, pictureBox17, pictureBox16, pictureBox15, pictureBox14, pictureBox34, pictureBox12, pictureBox11 },
                { pictureBox30, pictureBox29, pictureBox27, pictureBox61, pictureBox25, pictureBox25, pictureBox24, pictureBox23, pictureBox22, pictureBox21 },
                { pictureBox40, pictureBox39, pictureBox38, pictureBox37, pictureBox36, pictureBox35, pictureBox28, pictureBox33, pictureBox32, pictureBox31 },
                { pictureBox50, pictureBox49, pictureBox13, pictureBox47, pictureBox46, pictureBox45, pictureBox44, pictureBox43, pictureBox42, pictureBox41 },
                { pictureBox60, pictureBox59, pictureBox48, pictureBox57, pictureBox56, pictureBox55, pictureBox54, pictureBox53, pictureBox52, pictureBox51 }
            };

            for (int x = 0; x < 6; x++)
            {
                for (int y = 0; y < 10; y++)
                {
                    matrix[x, y].Click += StartEventHandler;
                }
            }

            label1.BackColor = Color.ForestGreen;
        }

        private void StartEventHandler(object sender, EventArgs e)
        {
            if (pickedStart)
            {
                PictureBox[,] matrix = new PictureBox[,]
                {
                { pictureBox1, pictureBox2, pictureBox3, pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9, pictureBox10 },
                { pictureBox20, pictureBox19, pictureBox18, pictureBox17, pictureBox16, pictureBox15, pictureBox14, pictureBox34, pictureBox12, pictureBox11 },
                { pictureBox30, pictureBox29, pictureBox27, pictureBox61, pictureBox25, pictureBox25, pictureBox24, pictureBox23, pictureBox22, pictureBox21 },
                { pictureBox40, pictureBox39, pictureBox38, pictureBox37, pictureBox36, pictureBox35, pictureBox28, pictureBox33, pictureBox32, pictureBox31 },
                { pictureBox50, pictureBox49, pictureBox13, pictureBox47, pictureBox46, pictureBox45, pictureBox44, pictureBox43, pictureBox42, pictureBox41 },
                { pictureBox60, pictureBox59, pictureBox48, pictureBox57, pictureBox56, pictureBox55, pictureBox54, pictureBox53, pictureBox52, pictureBox51 }
                };

                for (int x = 0; x < 6; x++)
                {
                    for (int y = 0; y < 10; y++)
                    {
                        matrix[x, y].Click += TargetEventHandler;
                    }
                }
                return;
            }

            pickedStart = true;
            PictureBox clickedPicture = (PictureBox)sender;

            label1.BackColor = Color.Transparent;
            label2.BackColor = Color.ForestGreen;

            // get name of clicked picture
            startingPoint = (PictureBox)sender;

            clickedPicture.BackColor = Color.PowderBlue;
        }

        private void TargetEventHandler(object sender, EventArgs e)
        {
            if (pickedTarget)
            {
                PictureBox[,] matrix = new PictureBox[,]
                {
                    { pictureBox1, pictureBox2, pictureBox3, pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9, pictureBox10 },
                    { pictureBox20, pictureBox19, pictureBox18, pictureBox17, pictureBox16, pictureBox15, pictureBox14, pictureBox34, pictureBox12, pictureBox11 },
                    { pictureBox30, pictureBox29, pictureBox27, pictureBox61, pictureBox25, pictureBox25, pictureBox24, pictureBox23, pictureBox22, pictureBox21 },
                    { pictureBox40, pictureBox39, pictureBox38, pictureBox37, pictureBox36, pictureBox35, pictureBox28, pictureBox33, pictureBox32, pictureBox31 },
                    { pictureBox50, pictureBox49, pictureBox13, pictureBox47, pictureBox46, pictureBox45, pictureBox44, pictureBox43, pictureBox42, pictureBox41 },
                    { pictureBox60, pictureBox59, pictureBox48, pictureBox57, pictureBox56, pictureBox55, pictureBox54, pictureBox53, pictureBox52, pictureBox51 }
                };

                for (int x = 0; x < 6; x++)
                {
                    for (int y = 0; y < 10; y++)
                    {
                        if(matrix[x,y] == startingPoint)
                        {
                            startX = x;
                            startY = y;
                        }
                        
                        if(matrix[x,y] == targetPoint)
                        {
                            targetX = x;
                            targetY = y;
                        }
                    }
                }

                SearchPath();
                return;
            }

            pickedTarget = true;
            PictureBox clickedPicture = (PictureBox)sender;

            label2.BackColor = Color.Transparent;

            // get name of clicked picture
            targetPoint = (PictureBox)sender;

            clickedPicture.BackColor = Color.BlueViolet;
        }

        private void SearchPath()
        {
            var worker = new BackgroundWorker();
            worker.DoWork += new DoWorkEventHandler(worker_DoWork);
            
            worker.RunWorkerAsync();
        }

        void worker_DoWork(object sender, DoWorkEventArgs e)
        {
            if (pathFound)
            {
                // stop           
                return;
            }

            PictureBox[,] matrix = new PictureBox[,]
            {
               { pictureBox1, pictureBox2, pictureBox3, pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9, pictureBox10 },
               { pictureBox20, pictureBox19, pictureBox18, pictureBox17, pictureBox16, pictureBox15, pictureBox14, pictureBox34, pictureBox12, pictureBox11 },
               { pictureBox30, pictureBox29, pictureBox27, pictureBox61, pictureBox25, pictureBox25, pictureBox24, pictureBox23, pictureBox22, pictureBox21 },
               { pictureBox40, pictureBox39, pictureBox38, pictureBox37, pictureBox36, pictureBox35, pictureBox28, pictureBox33, pictureBox32, pictureBox31 },
               { pictureBox50, pictureBox49, pictureBox13, pictureBox47, pictureBox46, pictureBox45, pictureBox44, pictureBox43, pictureBox42, pictureBox41 },
               { pictureBox60, pictureBox59, pictureBox48, pictureBox57, pictureBox56, pictureBox55, pictureBox54, pictureBox53, pictureBox52, pictureBox51 }
            };

            int x = startX;
            int y = startY;
            int closedListVar = 0;

            List<Tuple<PictureBox, int>> openList = new List<Tuple<PictureBox, int>>();
            List<Tuple<PictureBox, int>> closedList = new List<Tuple<PictureBox, int>>();

            // add start point to closedList
            closedList.Add(new Tuple<PictureBox, int>(matrix[x, y], 1));

            while (!pathFound)
            {
                // get current x and y 
                for (int i = 0; i < 6; i++)
                {
                    for (int j = 0; j < 10; j++)
                    {
                        if (matrix[i, j] == closedList[closedListVar].Item1)
                        {
                            x = i;
                            y = j;
                            break;
                        }
                    }
                }

                int rightScore = 0;
                int leftScore = 0;
                int upScore = 0;
                int downScore = 0;

                // count H distance for rightScore
                H = CalculateH(x, y + 1, targetX, targetY);
                rightScore = H;

                H = CalculateH(x, y - 1, targetX, targetY);
                leftScore = H;

                H = CalculateH(x - 1, y, targetX, targetY);
                upScore = H;
                
                H = CalculateH(x + 1, y, targetX, targetY);
                downScore = H;
                
                // increase distance from starting point
                G++;

                // count F(H+G)
                int resultRight = rightScore + G;
                int resultLeft = leftScore + G;
                int resultUp = upScore + G;
                int resultDown = downScore + G;

                if (y < 9)
                {
                    if ((string)matrix[x, y + 1].Tag == "moveAble")
                    {
                        openList.Add(new Tuple<PictureBox,int>(matrix[x, y + 1], resultRight));
                    }
                }

                if(y > 0)
                {
                    if ((string)matrix[x, y - 1].Tag == "moveAble")
                    {
                        openList.Add(new Tuple<PictureBox, int>(matrix[x, y - 1], resultLeft));
                    }
                }

                if(x > 0)
                {
                    if ((string)matrix[x - 1, y].Tag == "moveAble")
                    {
                        openList.Add(new Tuple<PictureBox, int>(matrix[x - 1, y], resultUp));
                    }
                }

                if(x < 5)
                {
                    if ((string)matrix[x + 1, y].Tag == "moveAble")
                    {
                        openList.Add(new Tuple<PictureBox, int>(matrix[x + 1, y], resultDown));
                    }
                }

                int least = resultRight;
                Tuple<PictureBox, int> item = openList[0];

                // dodaj do zamknietej listy pole z najmniejszym wynikiem
                for (int i = 0; i < openList.Count; i++)
                {
                    if(least > openList[i].Item2)
                    {
                        item = openList[i];
                    }
                }
                closedList.Add(item);

                if (x == targetX && y == targetY)
                {
                   pathFound = true;
                   break;
                }

                System.Threading.Thread.Sleep(1);
                closedListVar++;
                openList.Clear();
            }

            for(int temp = 1; temp < closedListVar; temp++)
            {
                closedList[temp].Item1.BackColor = Color.DarkSeaGreen;
                System.Threading.Thread.Sleep(1000);
            }
        }

        private int CalculateH(int x, int y, int targetX, int targetY)
        {
            // estimated distance to target
            return Math.Abs(targetX - x) + Math.Abs(targetY - y);

            // right = matrix[x, y + 1];
            // left = matrix[x, y - 1];
            // up = matrix[x - 1, y];
            // down = matrix[x + 1, y];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form1 newForm = new Form1();
            newForm.Show();
            this.Dispose(false);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
