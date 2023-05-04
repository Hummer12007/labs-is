using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KnowledgeBase
{
    internal class DataManager
    {
        List<Data> allData = new List<Data>();
        List<Rule> allRules = new List<Rule>();
        public bool AddNewData(string data)
        {
            if (SearchIndexOfData(data) != -1) return false;
            allData.Add(new Data(data));
            return true;
        }
        public bool AddOneWayConnectionToData(string from, string to, string connection)
        {
            int fromIndex = SearchIndexOfData(from);
            int toIndex = SearchIndexOfData(to);
            if (fromIndex < 0 || toIndex < 0) return false;
            Data fromData = allData[fromIndex];
            Data toData = allData[toIndex];
            fromData.AddConnection(new Connection(connection, toData));
            return true;
        }
        public bool AddTwoWayConnectionToData(string from, string to, string connection)
        {
            if (AddOneWayConnectionToData(from, to, connection) && AddOneWayConnectionToData(to, from, connection)) return true;
            return false;
        }
        public string ApplyRule(string from, string prompt, List<string> requiredConnections)
        {
            Rule rule = new Rule(requiredConnections, prompt);
            int fromIndex = SearchIndexOfData(from);
            if (fromIndex < 0 ) return "Specified data does not exist";
            Data fromData = allData[fromIndex];
            List<string> allPrompts = rule.ApplyRule(fromData);
            string result = "";
            foreach (string promptt in  allPrompts )
            {
                result += promptt;
            }
            return result;
        }
        public string ApplyRule(string from, string ruleName)
        {
            int fromIndex = SearchIndexOfData(from);
            if (fromIndex < 0) return "Specified data does not exist";
            int ruleIndex = SearchIndexOfRule(ruleName);
            if (ruleIndex < 0) return "Specified rule does not exist";
            Data fromData = allData[fromIndex];
            Rule rule = allRules[ruleIndex];
            List<string> allPrompts = rule.ApplyRule(fromData);
            string result = "";
            foreach (string promptt in allPrompts)
            {
                result += promptt;
            }
            return result;
        }
        public bool AddRule(string name, string prompt,  List<string> requiredConnections)
        {
            if (SearchIndexOfRule(name) != -1) return false;
            Rule rule = new Rule(name, requiredConnections, prompt);
            allRules.Add(rule);
            return true;
        }
        public string ShowAllData()
        {
            string res = "";
            foreach(Data data in allData)
            {
                res += data.data + '\n';
            }
            return res;
        }
        private int SearchIndexOfData(string dataName)
        {
            int i = 0;
            foreach (Data data in allData)
            {
                if (data.data == dataName)
                    return i;
                i++;
            }
            return -1;
        }
        private int SearchIndexOfRule(string ruleName)
        {
            int i = 0;
            foreach (Rule rule in allRules)
            {
                if (rule.name == ruleName)
                    return i;
                i++;
            }
            return -1;
        }
    }
}
