// The Spider Queen. She alone can spawn Spiderlings for each Player, and if she dies the owner loses.

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

namespace Joueur.cs.Games.Spiders
{
    /// <summary>
    /// The Spider Queen. She alone can spawn Spiderlings for each Player, and if she dies the owner loses.
    /// </summary>
    public class BroodMother : Spiders.Spider
    {
        #region Properties
        /// <summary>
        /// How many eggs the BroodMother has to spawn Spiderlings this turn.
        /// </summary>
        public int Eggs { get; protected set; }

        /// <summary>
        /// How much health this BroodMother has left. When it reaches 0, she dies and her owner loses.
        /// </summary>
        public int Health { get; protected set; }


        // <<-- Creer-Merge: properties -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional properties(s) here. None of them will be tracked or updated by the server.
        // <<-- /Creer-Merge: properties -->>
        #endregion


        #region Methods
        /// <summary>
        /// Creates a new instance of BroodMother. Used during game initialization, do not call directly.
        /// </summary>
        protected BroodMother() : base()
        {
        }

        /// <summary>
        /// Consumes a Spiderling of the same owner to regain some eggs to spawn more Spiderlings.
        /// </summary>
        /// <param name="spiderling">The Spiderling to consume. It must be on the same Nest as this BroodMother.</param>
        /// <returns>True if the Spiderling was consumed. False otherwise.</returns>
        public bool Consume(Spiders.Spiderling spiderling)
        {
            return this.RunOnServer<bool>("consume", new Dictionary<string, object> {
                {"spiderling", spiderling}
            });
        }

        /// <summary>
        /// Spawns a new Spiderling on the same Nest as this BroodMother, consuming an egg.
        /// </summary>
        /// <param name="spiderlingType">The string name of the Spiderling class you want to Spawn. Must be 'Spitter', 'Weaver', or 'Cutter'.</param>
        /// <returns>The newly spawned Spiderling if successful. Null otherwise.</returns>
        public Spiders.Spiderling Spawn(string spiderlingType)
        {
            return this.RunOnServer<Spiders.Spiderling>("spawn", new Dictionary<string, object> {
                {"spiderlingType", spiderlingType}
            });
        }


        // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional method(s) here.
        // <<-- /Creer-Merge: methods -->>
        #endregion
    }
}
