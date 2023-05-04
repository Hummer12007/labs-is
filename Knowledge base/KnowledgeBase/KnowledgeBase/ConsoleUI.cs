using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KnowledgeBase
{
    internal class ConsoleUI
    {
        CommandManager commandManager = new CommandManager();
        public ConsoleUI(CommandManager commandManager) 
        {
            this.commandManager = commandManager;
        }

        bool quit = false;
        public void StartConsole()
        {
            do
            {
                Console.Write(">> ");
                ParseAndExecute(Console.ReadLine());
            } while (!quit);
        }
        public void ParseAndExecute(string commandLine)
        {
            string[] splited = commandLine.Split('"');
            int i = 0;
            List<string> args = new List<string>();
            foreach (string s in splited)
            {
                if (i%2 == 0) 
                {
                    if (!string.IsNullOrWhiteSpace(s)) 
                        foreach (string s2 in s.Trim().Split(' '))
                        {
                            args.Add(s2);
                        }
                }
                else
                {
                    args.Add(s);
                }
                i++;
            }
            string[] parsed = args.ToArray();
            string message = commandManager.Execute(parsed[0], parsed.Skip(1).ToArray());
            Console.WriteLine(message);
            if (parsed[0].ToLower() == "exit")
                quit = true;
        }
        
    }
}
