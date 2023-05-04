using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KnowledgeBase
{
    internal class Data
    {
        public string data { get; set; }
        public List<Connection> connections { get; }
        public Data()
        {
            data = "";
            connections = new List<Connection>();
        }
        public Data(string data)
        {
            this.data = data;
            this.connections = new List<Connection>();
        }
        public Data(string data, List<Connection> connections)
        {
            this.data = data;
            this.connections = new List<Connection>(connections);
        }
        public void AddConnection(Connection connection)
        {
            connections.Add(connection);
        }
    }
}
