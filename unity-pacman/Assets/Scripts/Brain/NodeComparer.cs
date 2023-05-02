using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assets.Scripts.Brain
{
    internal class NodeComparer : IComparer<(List<string>, int, int, string)>
    {
        public int Compare((List<string>, int, int, string) x, (List<string>, int, int, string) y)
        {
            return x.Item2.CompareTo(y.Item2);
        }
    }
}
