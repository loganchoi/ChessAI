#ifndef GAMES_COREMINER_PLAYER_H
#define GAMES_COREMINER_PLAYER_H

// Player
// A player in this game. Every AI controls one player.

// DO NOT MODIFY THIS FILE
// Never try to directly create an instance of this class, or modify its member variables.
// Instead, you should only be reading its variables and calling its functions.

#include <vector>
#include <queue>
#include <deque>
#include <unordered_map>
#include <string>
#include <initializer_list>

#include "../../joueur/src/any.hpp"

#include "game_object.hpp"

#include "impl/coreminer_fwd.hpp"

// <<-- Creer-Merge: includes -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
// you can add additional #includes here
// <<-- /Creer-Merge: includes -->>

namespace cpp_client
{

namespace coreminer
{

/// <summary>
/// A player in this game. Every AI controls one player.
/// </summary>
class Player_ : public Game_object_
{
public:

    /// <summary>
    /// The Tile this Player's base is on.
    /// </summary>
    const Tile& base_tile;

    /// <summary>
    /// Every Bomb owned by this Player.
    /// </summary>
    const std::vector<Bomb>& bombs;

    /// <summary>
    /// What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
    /// </summary>
    const std::string& client_type;

    /// <summary>
    /// The Tiles this Player's hoppers are on.
    /// </summary>
    const std::vector<Tile>& hopper_tiles;

    /// <summary>
    /// If the player lost the game or not.
    /// </summary>
    const bool& lost;

    /// <summary>
    /// Every Miner owned by this Player.
    /// </summary>
    const std::vector<Miner>& miners;

    /// <summary>
    /// The amount of money this Player currently has.
    /// </summary>
    const int& money;

    /// <summary>
    /// The name of the player.
    /// </summary>
    const std::string& name;

    /// <summary>
    /// This player's opponent in the game.
    /// </summary>
    const Player& opponent;

    /// <summary>
    /// The reason why the player lost the game.
    /// </summary>
    const std::string& reason_lost;

    /// <summary>
    /// The reason why the player won the game.
    /// </summary>
    const std::string& reason_won;

    /// <summary>
    /// The amount of time (in ns) remaining for this AI to send commands.
    /// </summary>
    const double& time_remaining;

    /// <summary>
    /// The amount of value (victory points) this Player has gained.
    /// </summary>
    const int& value;

    /// <summary>
    /// If the player won the game or not.
    /// </summary>
    const bool& won;

    // <<-- Creer-Merge: member variables -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    // You can add additional member variables here. None of them will be tracked or updated by the server.
    // <<-- /Creer-Merge: member variables -->>


    /// <summary>
    /// spawns a _miner on this _player's base _tile.
    /// </summary>
    bool spawn_miner();


   // <<-- Creer-Merge: methods -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
   // You can add additional methods here.
   // <<-- /Creer-Merge: methods -->>

   ~Player_();

   // ####################
   // Don't edit these!
   // ####################
   /// \cond FALSE
   Player_(std::initializer_list<std::pair<std::string, Any&&>> init);
   Player_() : Player_({}){}
   virtual void resize(const std::string& name, std::size_t size) override;
   virtual void change_vec_values(const std::string& name, std::vector<std::pair<std::size_t, Any>>& values) override;
   virtual void remove_key(const std::string& name, Any& key) override;
   virtual std::unique_ptr<Any> add_key_value(const std::string& name, Any& key, Any& value) override;
   virtual bool is_map(const std::string& name) override;
   virtual void rebind_by_name(Any* to_change, const std::string& member, std::shared_ptr<Base_object> ref) override;
    /// \endcond
    // ####################
    // Don't edit these!
    // ####################
};

} // coreminer

} // cpp_client

#endif // GAMES_COREMINER_PLAYER_H
