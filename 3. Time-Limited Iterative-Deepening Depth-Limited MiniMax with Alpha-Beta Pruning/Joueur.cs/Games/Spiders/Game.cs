// There's an infestation of enemy spiders challenging your queen BroodMother spider! Protect her and attack the other BroodMother in this turn based, node based, game.

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

/// <summary>
/// There's an infestation of enemy spiders challenging your queen BroodMother spider! Protect her and attack the other BroodMother in this turn based, node based, game.
/// </summary>
namespace Joueur.cs.Games.Spiders
{
    /// <summary>
    /// There's an infestation of enemy spiders challenging your queen BroodMother spider! Protect her and attack the other BroodMother in this turn based, node based, game.
    /// </summary>
    public class Game : BaseGame
    {
        /// <summary>
        /// The game version hash, used to compare if we are playing the same version on the server.
        /// </summary>
        new protected static string GameVersion = "a8df6038306b6855bb35959d7698f8dcbf98f48e7e148de59fef940ccb241bdf";

        #region Properties
        /// <summary>
        /// The player whose turn it is currently. That player can send commands. Other players cannot.
        /// </summary>
        public Spiders.Player CurrentPlayer { get; protected set; }

        /// <summary>
        /// The current turn number, starting at 0 for the first player's turn.
        /// </summary>
        public int CurrentTurn { get; protected set; }

        /// <summary>
        /// The speed at which Cutters work to do cut Webs.
        /// </summary>
        public int CutSpeed { get; protected set; }

        /// <summary>
        /// Constant used to calculate how many eggs BroodMothers get on their owner's turns.
        /// </summary>
        public double EggsScalar { get; protected set; }

        /// <summary>
        /// The starting strength for Webs.
        /// </summary>
        public int InitialWebStrength { get; protected set; }

        /// <summary>
        /// The maximum number of turns before the game will automatically end.
        /// </summary>
        public int MaxTurns { get; protected set; }

        /// <summary>
        /// The maximum strength a web can be strengthened to.
        /// </summary>
        public int MaxWebStrength { get; protected set; }

        /// <summary>
        /// The speed at which Spiderlings move on Webs.
        /// </summary>
        public int MovementSpeed { get; protected set; }

        /// <summary>
        /// Every Nest in the game.
        /// </summary>
        public IList<Spiders.Nest> Nests { get; protected set; }

        /// <summary>
        /// List of all the players in the game.
        /// </summary>
        public IList<Spiders.Player> Players { get; protected set; }

        /// <summary>
        /// A unique identifier for the game instance that is being played.
        /// </summary>
        public string Session { get; protected set; }

        /// <summary>
        /// The speed at which Spitters work to spit new Webs.
        /// </summary>
        public int SpitSpeed { get; protected set; }

        /// <summary>
        /// The amount of time (in nano-seconds) added after each player performs a turn.
        /// </summary>
        public int TimeAddedPerTurn { get; protected set; }

        /// <summary>
        /// How much web strength is added or removed from Webs when they are weaved.
        /// </summary>
        public int WeavePower { get; protected set; }

        /// <summary>
        /// The speed at which Weavers work to do strengthens and weakens on Webs.
        /// </summary>
        public int WeaveSpeed { get; protected set; }

        /// <summary>
        /// Every Web in the game.
        /// </summary>
        public IList<Spiders.Web> Webs { get; protected set; }


        // <<-- Creer-Merge: properties -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional properties(s) here. None of them will be tracked or updated by the server.
        // <<-- /Creer-Merge: properties -->>
        #endregion


        #region Methods
        /// <summary>
        /// Creates a new instance of Game. Used during game initialization, do not call directly.
        /// </summary>
        protected Game() : base()
        {
            this.Name = "Spiders";

            this.Nests = new List<Spiders.Nest>();
            this.Players = new List<Spiders.Player>();
            this.Webs = new List<Spiders.Web>();
        }


        // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional method(s) here.
        // <<-- /Creer-Merge: methods -->>
        #endregion
    }
}
