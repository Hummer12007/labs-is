using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KnowledgeBase
{
    internal class CommandManager
    {
        static Dictionary<Func<string[], string>, string> commands = new()
        {
            {Help, "shows the list of commands" },
            {Exit, "exits the program" },
            {ShowAllData, "Shows all data entries" },
            {AddData, "arguments: <data>. adds new data to the knowledge base" },
            {AddOneWayConnection, "arguments: <from Data> <to Data> <connection Name>. Adds one way connection from <fromData> to <toData>" },
            {AddTwoWayConnection, "arguments: <first Data> <second Data> <connection Name>. Adds two way connection between <firstData> and <secondData>" },
            {ApplyBlindRule, "arguments: <data> <prompt> <required connection> [additional required connections]. Applies rule without adding it to the base" },
            {AddNewRule, "arguments: <name> <prompt> <required connection> [additional required connections]. Adds rule to the base" },
            {ApplyRule, "arguments: <from Data> <rule name>. Applies rule that has been added to the base " }
        };
        static DataManager dataManager = new DataManager();
        public CommandManager() { }
        public string Execute(string commandName, string[] args) 
        {
            foreach (KeyValuePair<Func<string[], string>, string> commandWithDescription in commands)
            {
                if (commandWithDescription.Key.Method.Name.ToLower() == commandName.ToLower())
                    return commandWithDescription.Key(args);
            }
            return "Invalid command, enter 'help' to see the list of commands";
        }
        private static string Help(string[] arguments)
        {
            string result = "";
            foreach (KeyValuePair<Func<string[], string>, string> commandWithDescription in commands)
            {
                result += commandWithDescription.Key.Method.Name + ": " + commandWithDescription.Value + '\n';
            }
            return result;
        }
        private static string Exit(string[] arguments)
        {
            return "Exiting...";
        }
        private static string AddData(string[] arguments)
        {
            if (arguments[0] is null)
                return "Argument Error";
            if (!dataManager.AddNewData(arguments[0]))
                return "This data already exists";
            else
                return "Added data succesfully";
        }
        private static string AddOneWayConnection(string[] arguments)
        {
            if (arguments[0] is null || arguments[1] is null || arguments[2] is null)
                return "Argument Error";
            if (!dataManager.AddOneWayConnectionToData(arguments[0], arguments[1], arguments[2]))
                return "Specified data does not exist";
            else
                return "Added one way connection succesfully";
        }
        private static string AddTwoWayConnection(string[] arguments)
        {
            if (arguments[0] is null || arguments[1] is null || arguments[2] is null)
                return "Argument Error";
            if (!dataManager.AddTwoWayConnectionToData(arguments[0], arguments[1], arguments[2]))
                return "Specified data does not exist";
            else
                return "Added one way connection succesfully";
        }
        private static string ApplyBlindRule(string[] arguments)
        {
            if (arguments[0] is null || arguments[1] is null || arguments[2] is null)
                return "Argument Error";
            List<string> reqc = arguments.Skip(2).ToList();
            return dataManager.ApplyRule(arguments[0], arguments[1], reqc);
        }
        private static string AddNewRule(string[] arguments)
        {
            if (arguments[0] is null || arguments[1] is null || arguments[2] is null)
                return "Argument Error";
            List<string> reqc = arguments.Skip(2).ToList();
            if (!dataManager.AddRule(arguments[0], arguments[1], reqc))
                return "This rule already exists";
            else
                return "Added rule succesfully";
        }
        private static string ApplyRule(string[] arguments)
        {
            if (arguments[0] is null || arguments[1] is null)
                return "Argument Error";
            return dataManager.ApplyRule(arguments[0], arguments[1]);
        }
        private static string ShowAllData(string[] arguments)
        {
            return dataManager.ShowAllData();
        }
    }        
}
