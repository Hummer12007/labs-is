using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;

namespace Assets.Scripts.Brain
{
    public interface IPacmanLogic
    {
        public abstract List<string> FindWay(Transform target, Transform pacman);

    }
}
