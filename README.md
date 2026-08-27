<div align="center">

# OUTTRIGGER Remake

### An unofficial remake of SEGA's arena shooter, built with Unreal Engine 5

[![Unreal Engine](https://img.shields.io/badge/Unreal_Engine-5.8-0E1128?style=for-the-badge&logo=unrealengine&logoColor=white)](https://www.unrealengine.com/)
[![Blueprints](https://img.shields.io/badge/Blueprints-100%25-137CBD?style=for-the-badge&logo=unrealengine&logoColor=white)](#tech-stack)
[![Status](https://img.shields.io/badge/Status-In_Development-F59E0B?style=for-the-badge)](#development-status)

A fast-paced first/third-person shooter featuring an extensible weapon system, arena pickups, power-ups, aim assist, and a responsive HUD inspired by the original **OUTTRIGGER**.

</div>

> [!IMPORTANT]
> This project is under active development. Gameplay systems, balance, visuals, controls, and asset organization are subject to change.

## About the project

**OUTTRIGGER Remake** is a fan-made project that aims to recreate the pace and core gameplay ideas of OUTTRIGGER using Unreal Engine 5.

The current build focuses on the foundation of the combat loop: moving around a prototype arena, switching between first- and third-person views, firing and swapping weapons, taking damage, respawning, collecting resources and power-ups, and receiving immediate feedback through the HUD.

## Current features

### Player and combat

- First- and third-person camera modes
- Character movement and jumping
- Modular health and weapon components
- Damage, armor, death, and respawn systems
- Reserved spawn points to prevent conflicting respawns
- Aim assist with crosshair feedback
- Projectile ownership and teammate-damage protection

### Weapons

- Shared base classes for hitscan and projectile weapons
- Weapon slots and independent ammunition pools
- Configurable fire types, launch modes, states, and ammo cost per shot
- Rifle
- Grenade launcher framework
- Rocket/projectile launcher framework
- Photon Torpedo with a dedicated pickup and projectile
- Sniper Rifle with a scope HUD and a pickup placed in the arena
- Flamethrower with continuous, fractional ammunition consumption
- Standard, Heavy, and Sensor Bomb grenade variants
- Physics-driven grenade movement with configurable surface behavior

### Pickups and HUD

- Health, armor, and ammunition pickups
- Eagle power-up
- Pickable special weapons
- Health and armor display with damage, healing, and low-health feedback
- Weapon slots, temporary weapon icons, and current ammunition display
- Weapon-specific crosshairs
- Scope overlay for the Sniper Rifle
- Low-ammo and aim-assist visual feedback

## Controls

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | `W` `A` `S` `D` | Left stick |
| Look | Mouse | Right stick |
| Jump | `Space` | Bottom face button |
| Fire | Left mouse button | Not mapped yet |
| Next weapon | Mouse wheel up | Not mapped yet |
| Previous weapon | Mouse wheel down | Not mapped yet |
| Toggle first/third-person view | `V` | Not mapped yet |

Input is implemented with Unreal Engine's Enhanced Input system. Gamepad support is currently partial.

## Tech stack

- **Unreal Engine 5.8**
- **Blueprints**
- **Enhanced Input**
- **UMG** for the HUD and scope interface
- **Git LFS** for `.uasset` and `.umap` files

## Getting started

### Requirements

- Unreal Engine **5.8**
- Git
- [Git LFS](https://git-lfs.com/)
- Windows 10 or 11
- A DirectX 12-compatible GPU; ray-tracing-capable hardware is recommended for the current renderer settings

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Biryuk666/OUTTRIGGER-Remake.git
   cd OUTTRIGGER-Remake
   ```

2. Install Git LFS hooks and download the binary assets:

   ```bash
   git lfs install
   git lfs pull
   ```

3. Open `OUTTRIGGER.uproject` with Unreal Engine 5.8.

4. Allow the editor to discover assets and compile shaders. The default map is:

   ```text
   /Game/OUTTRIGGER/Maps/ThirdPersonMap
   ```

5. Press **Play** in the Unreal Editor.

> [!NOTE]
> `Binaries`, `Intermediate`, `DerivedDataCache`, and `Saved` are generated locally by Unreal Engine and are not stored in the repository.

## Project structure

```text
OUTTRIGGER-Remake/
|-- Config/                         # Project, input, and renderer settings
|-- Content/
|   `-- OUTTRIGGER/
|       |-- Anims/                  # Character and weapon animations
|       |-- Blueprints/
|       |   |-- Components/         # Health and weapon components
|       |   |-- Pickups/            # Resources, power-ups, and weapon pickups
|       |   `-- Weapons/            # Weapons, grenades, and projectiles
|       |-- Characters/             # Character meshes, materials, and animations
|       |-- Input/                  # Enhanced Input actions and mapping context
|       |-- LevelPrototyping/       # Blockout materials and meshes
|       |-- Maps/                   # Playable maps
|       |-- PhysicsMaterials/       # Character and projectile physics materials
|       |-- UI/                     # HUD, crosshairs, scope, and weapon slots
|       `-- Weapons/                # Weapon meshes, materials, and textures
|-- Plugins/                        # Project-specific plugins
`-- OUTTRIGGER.uproject
```

## Development status

- [x] Core movement and camera switching
- [x] Health, armor, damage, death, and respawning
- [x] Hitscan and projectile weapon foundations
- [x] Weapon switching, slots, and ammo pools
- [x] Resource, power-up, and special-weapon pickups
- [x] Aim assist and combat HUD
- [x] Photon Torpedo
- [x] Heavy Grenade and Sensor Bomb foundations
- [x] Sniper Rifle and scope HUD
- [x] Flamethrower foundation
- [ ] Complete weapon roster
- [ ] Final arena and environment art
- [ ] Enemies and a complete match flow
- [ ] Audio, VFX, animation, and gameplay polish
- [ ] Public test build

## Contributing and feedback

The project is still evolving. If you encounter a bug or want to suggest an improvement, please [open an issue](https://github.com/Biryuk666/OUTTRIGGER-Remake/issues).

## Legal notice

This is an unofficial, non-commercial fan project. It is not affiliated with, endorsed by, or sponsored by SEGA or the rights holders of the original OUTTRIGGER. All trademarks and referenced properties belong to their respective owners.

---

<div align="center">

**Made with Unreal Engine**

</div>
