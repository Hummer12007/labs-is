using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KnowledgeBase
{
    internal class Connection
    {
        public string name;
        public Data connectsTo;
        public Connection()
        {
            name = string.Empty;
            connectsTo = new Data();
        }
        public Connection(string name, Data connectsTo)
        {
            this.name = name;
            this.connectsTo = connectsTo;
        }
    }
}
