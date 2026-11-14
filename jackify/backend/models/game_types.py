"""Canonical game type strings, display names, and normalisation helpers."""

from typing import Optional

# Maps Jackify canonical game_type -> human-readable display name
GAME_DISPLAY_NAMES: dict[str, str] = {
    'skyrim': 'Skyrim Special Edition',
    'fallout4': 'Fallout 4',
    'falloutnv': 'Fallout New Vegas',
    'fallout3': 'Fallout 3',
    'oblivion': 'Oblivion',
    'oblivion_remastered': 'Oblivion Remastered',
    'starfield': 'Starfield',
    'enderal': 'Enderal',
    'skyrimvr': 'Skyrim VR',
    'fallout4vr': 'Fallout 4 VR',
    'bg3': "Baldur's Gate 3",
    'cp2077': 'Cyberpunk 2077',
    'witcher3': 'The Witcher 3',
}

# Maps lowercased human-readable / alternate name -> canonical game_type
GAME_NAME_TO_TYPE: dict[str, str] = {
    'skyrim special edition': 'skyrim',
    'skyrim': 'skyrim',
    'skyrimspecialedition': 'skyrim',
    'fallout 4': 'fallout4',
    'fallout4': 'fallout4',
    'fallout new vegas': 'falloutnv',
    'falloutnv': 'falloutnv',
    'fallout 3': 'fallout3',
    'fallout3': 'fallout3',
    'oblivion': 'oblivion',
    'oblivion remastered': 'oblivion_remastered',
    'oblivion_remastered': 'oblivion_remastered',
    'oblivionremastered': 'oblivion_remastered',
    'starfield': 'starfield',
    'enderal': 'enderal',
    'enderal special edition': 'enderal',
    'enderalspecialedition': 'enderal',
    'skyrim vr': 'skyrimvr',
    'skyrimvr': 'skyrimvr',
    'fallout 4 vr': 'fallout4vr',
    'fallout4vr': 'fallout4vr',
    "baldur's gate 3": 'bg3',
    'baldursgate3': 'bg3',
    'bg3': 'bg3',
    'cyberpunk 2077': 'cp2077',
    'cyberpunk2077': 'cp2077',
    'cp2077': 'cp2077',
    # Wabbajack's gallery calls it "Witcher 3"; MO2's game plugin writes
    # gameName=The Witcher 3: Wild Hunt into ModOrganizer.ini.
    'witcher 3': 'witcher3',
    'witcher3': 'witcher3',
    'the witcher 3': 'witcher3',
    'the witcher 3: wild hunt': 'witcher3',
    'the witcher 3 wild hunt': 'witcher3',
    'witcher 3: wild hunt': 'witcher3',
}


def normalize_game_name(raw: str) -> Optional[str]:
    """Return canonical game_type for a raw name, or None if unrecognised."""
    if not raw:
        return None
    return GAME_NAME_TO_TYPE.get(raw.lower())
