// A player in this game. Every AI controls one player.

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
    /// A player in this game. Every AI controls one player.
    /// </summary>
    public class Player : Anarchy.GameObject
    {
        #region Properties
        /// <summary>
        /// How many bribes this player has remaining to use during their turn. Each action a Building does costs 1 bribe. Any unused bribes are lost at the end of the player's turn.
        /// </summary>
        public int BribesRemaining { get; protected set; }

        /// <summary>
        /// All the buildings owned by this player.
        /// </summary>
        public IList<Anarchy.Building> Buildings { get; protected set; }

        /// <summary>
        /// What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
        /// </summary>
        public string ClientType { get; protected set; }

        /// <summary>
        /// All the FireDepartments owned by this player.
        /// </summary>
        public IList<Anarchy.FireDepartment> FireDepartments { get; protected set; }

        /// <summary>
        /// The Warehouse that serves as this player's headquarters and has extra health. If this gets destroyed they lose.
        /// </summary>
        public Anarchy.Warehouse Headquarters { get; protected set; }

        /// <summary>
        /// If the player lost the game or not.
        /// </summary>
        public bool Lost { get; protected set; }

        /// <summary>
        /// The name of the player.
        /// </summary>
        public string Name { get; protected set; }

        /// <summary>
        /// This player's opponent in the game.
        /// </summary>
        public Anarchy.Player Opponent { get; protected set; }

        /// <summary>
        /// All the PoliceDepartments owned by this player.
        /// </summary>
        public IList<Anarchy.PoliceDepartment> PoliceDepartments { get; protected set; }

        /// <summary>
        /// The reason why the player lost the game.
        /// </summary>
        public string ReasonLost { get; protected set; }

        /// <summary>
        /// The reason why the player won the game.
        /// </summary>
        public string ReasonWon { get; protected set; }

        /// <summary>
        /// The amount of time (in ns) remaining for this AI to send commands.
        /// </summary>
        public double TimeRemaining { get; protected set; }

        /// <summary>
        /// All the warehouses owned by this player. Includes the Headquarters.
        /// </summary>
        public IList<Anarchy.Warehouse> Warehouses { get; protected set; }

        /// <summary>
        /// All the WeatherStations owned by this player.
        /// </summary>
        public IList<Anarchy.WeatherStation> WeatherStations { get; protected set; }

        /// <summary>
        /// If the player won the game or not.
        /// </summary>
        public bool Won { get; protected set; }


        // <<-- Creer-Merge: properties -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional properties(s) here. None of them will be tracked or updated by the server.
        // <<-- /Creer-Merge: properties -->>
        #endregion


        #region Methods
        /// <summary>
        /// Creates a new instance of Player. Used during game initialization, do not call directly.
        /// </summary>
        protected Player() : base()
        {
            this.Buildings = new List<Anarchy.Building>();
            this.FireDepartments = new List<Anarchy.FireDepartment>();
            this.PoliceDepartments = new List<Anarchy.PoliceDepartment>();
            this.Warehouses = new List<Anarchy.Warehouse>();
            this.WeatherStations = new List<Anarchy.WeatherStation>();
        }


        // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional method(s) here.
        // <<-- /Creer-Merge: methods -->>
        #endregion
    }
}
