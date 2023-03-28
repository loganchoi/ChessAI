// Information about a unit's job.

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

namespace Joueur.cs.Games.Stardash
{
    /// <summary>
    /// Information about a unit's job.
    /// </summary>
    public class Job : Stardash.GameObject
    {
        #region Properties
        /// <summary>
        /// How many combined resources a unit with this Job can hold at once.
        /// </summary>
        public int CarryLimit { get; protected set; }

        /// <summary>
        /// The amount of damage this Job does per attack.
        /// </summary>
        public int Damage { get; protected set; }

        /// <summary>
        /// The amount of starting health this Job has.
        /// </summary>
        public int Energy { get; protected set; }

        /// <summary>
        /// The distance this job can move per turn.
        /// </summary>
        public int Moves { get; protected set; }

        /// <summary>
        /// The distance at which this job can effect things.
        /// </summary>
        public int Range { get; protected set; }

        /// <summary>
        /// The reserve the martyr use to protect allies.
        /// </summary>
        public int Shield { get; protected set; }

        /// <summary>
        /// The Job title. 'corvette', 'missileboat', 'martyr', 'transport', or 'miner'. (in this order from 0-4).
        /// </summary>
        public string Title { get; protected set; }

        /// <summary>
        /// How much money it costs to spawn a unit.
        /// </summary>
        public int UnitCost { get; protected set; }


        // <<-- Creer-Merge: properties -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional properties(s) here. None of them will be tracked or updated by the server.
        // <<-- /Creer-Merge: properties -->>
        #endregion


        #region Methods
        /// <summary>
        /// Creates a new instance of Job. Used during game initialization, do not call directly.
        /// </summary>
        protected Job() : base()
        {
        }


        // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional method(s) here.
        // <<-- /Creer-Merge: methods -->>
        #endregion
    }
}
