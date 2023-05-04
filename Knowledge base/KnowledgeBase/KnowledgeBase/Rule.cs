using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KnowledgeBase
{
    internal class Rule
    {
        public string name;
        List<string> requiredConnections;
        string prompt;
        List<string> applicationResults= new();
        public Rule(List<string> requiredConnections, string prompt) 
        {
            name = "temp";
            this.requiredConnections = new List<string>(requiredConnections);
            this.prompt = prompt;
        }
        public Rule(string name, List<string> requiredConnections, string prompt)
        {
            this.name = name;
            this.requiredConnections = new List<string>(requiredConnections);
            this.prompt = prompt;
        }
        public bool CheckIfApplies(List<string> connections)
        {
            return Enumerable.SequenceEqual(requiredConnections, connections);
        }
        public List<string> ApplyRule(Data data) 
        {
            applicationResults.Clear();
            IterateRule(new List<string>(), data, 0);
            return applicationResults;
        }
        public void IterateRule(List<string> visitedData, Data data, int fromPoint)
        {
            if (fromPoint == requiredConnections.Count)
            {
                applicationResults.Add(prompt + " " + data.data);
                return;
            }
            foreach (Connection connection in data.connections)
            {
                if(connection.name == requiredConnections[fromPoint])
                    if (!visitedData.Contains(connection.connectsTo.data))
                    {
                        List<string> clonedVisited = new List<string>(visitedData);
                        clonedVisited.Add(connection.connectsTo.data);
                        IterateRule(clonedVisited, connection.connectsTo, fromPoint + 1);
                    }
            }
        }

    }
}
