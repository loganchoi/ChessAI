// A Spiderling that creates and spits new Webs from the Nest it is on to another Nest, connecting them.

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
    /// A Spiderling that creates and spits new Webs from the Nest it is on to another Nest, connecting them.
    /// </summary>
    public class Spitter : Spiders.Spiderling
    {
        #region Properties
        /// <summary>
        /// The Nest that this Spitter is creating a Web to spit at, thus connecting them. Null if not spitting.
        /// </summary>
        public Spiders.Nest SpittingWebToNest { get; protected set; }


        // <<-- Creer-Merge: properties -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional properties(s) here. None of them will be tracked or updated by the server.
        // <<-- /Creer-Merge: properties -->>
        #endregion


        #region Methods
        /// <summary>
        /// Creates a new instance of Spitter. Used during game initialization, do not call directly.
        /// </summary>
        protected Spitter() : base()
        {
        }

        /// <summary>
        /// Creates and spits a new Web from the Nest the Spitter is on to another Nest, connecting them.
        /// </summary>
        /// <param name="nest">The Nest you want to spit a Web to, thus connecting that Nest and the one the Spitter is on.</param>
        /// <returns>True if the spit was successful, false otherwise.</returns>
        public bool Spit(Spiders.Nest nest)
        {
            return this.RunOnServer<bool>("spit", new Dictionary<string, object> {
                {"nest", nest}
            });
        }


        // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        // you can add additional method(s) here.
        // <<-- /Creer-Merge: methods -->>
        #endregion
    }
}
