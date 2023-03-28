// The weather effect that will be applied at the end of a turn, which causes fires to spread.

// DO NOT MODIFY THIS FILE
// Never try to directly create an instance of this class, or modify its member variables.
// Instead, you should only be reading its variables and calling its functions.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
// <<-- Creer-Merge: usings -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
// you can add additional using(s) here
// <<-- /Creer-Merge: usings -->>

namespace Joueur.cs.Games.Anarchy
{
    /// <summary>
    /// The weather effect that will be applied at the end of a turn, which causes fires to spread.
    /// </summary>
    public class Forecast : Anarchy.GameObject
    {
        #region Properties
        /// <summary>
        /// The Player that can use WeatherStations to control this Forecast when its the nextForecast.
        /// </summary>
        public Anarchy.Player ControllingPlayer { get; protected set; }

        /// <summary>
        /// The direction the wind will blow fires in. Can be 'north', 'east', 'south', or 'west'.
        /// </summary>
        public string Direction { get; protected set; }

        /// <summary>
        /// How much of a Building's fire that can be blown in the direction of this Forecast. Fire is duplicated (copied), not moved (transferred).
        /// </summary>
        public int Intensity { get; protected set; }


        // <<-- Creer-Merge: properties -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional properties(s) here. None of them will be tracked or updated by the server.
        // <<-- /Creer-Merge: properties -->>
        #endregion


        #region Methods
        /// <summary>
        /// Creates a new instance of Forecast. Used during game initialization, do not call directly.
        /// </summary>
        protected Forecast() : base()
        {
        }


        // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional method(s) here.
        // <<-- /Creer-Merge: methods -->>
        #endregion
    }
}
