using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
        // xChange and yChange represent the cursor moves on the x and y axis
        // Example: xChange + 1 = the cursor moves to the right by 1 unit
        public new static void UpdatePosition(string key, out int xChange, out int yChange)
        {    
            // Because our out var are inside an if statement we need to initialize them outside the statement since the method needs to be sure that we bring them "out"
            xChange = 0;
            yChange = 0;

            switch (key)
            {
                case "LeftArrow":
                    xChange--;
                    break;
                case "RightArrow":
                    xChange++;
                    break;
                case "UpArrow":
                    yChange--;
                    break;
                case "DownArrow":
                    yChange++;
                    break;
            }
        }

        public new static char UpdateCursor(string key)
        {
            switch (key)
            {
                case "LeftArrow":
                    return '<';
                case "RightArrow":
                    return '>';
                case "UpArrow":
                    return '^';
                case "DownArrow":
                    return 'v';
                default:
                    return '<';
            }
        }


        // This method is called twice in Program, once for the x axis (characterCol) and once for the y axis (characterRow)
        // Makes sure the game doesn't crash if the cursor reach the border
        public new static int KeepInBounds(int dimension, int max)
        {
            // We can teleport the cursor to the other side swapping the return statement: if (dimension < 0) return max;
            if (dimension < 0)
            {
                return 0;
            }
            else if (dimension > max)
            {
                return max;
            }
            else
            {
                return dimension;
            }
        }


        // Return true if the cursor reach the fruit
        public new static bool DidScore(int xChar, int yChar, int xFruit, int yFruit)
        {
            return xChar == xFruit && yChar == yFruit;
        }
    }
}