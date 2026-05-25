#!/usr/bin/env python3
"""
Batch downloader for poe2db.tw unique item pages.
Saves each unique as raw/poe2db/uniques/{slug}.md
"""

import requests
import time
import os
import re
from datetime import date
from bs4 import BeautifulSoup
from urllib.parse import unquote

BASE_URL = "https://poe2db.tw/us/"
OUT_DIR = os.path.join(os.path.dirname(__file__), "uniques")
TODAY = date.today().isoformat()
PATCH = "0.4.0"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

SLUGS = [
    "Brynhands_Mark","Frostbreath","Trenchtimbre","Sculpted_Suffering","Nebuloch",
    "Mj%C3%B6lner","Thundergods_Wrath","Olrovasara","Hoghunt","Hrimnors_Hymn",
    "Trephina","Brain_Rattler","The_Empty_Roar","Shyaba","Chober_Chaber",
    "Quecholli","Tidebreaker","Marohi_Erqi","The_Hammer_of_Faith","Splinter_of_Lorrata",
    "Spear_Throw","Tyrannys_Grip","Chainsting","Skysliver","Daevatas_Wind",
    "Tangletongue","Saithas_Spear","Spire_of_Ire","Chaotic_Surge","The_Blood_Thorn",
    "Pillar_of_the_Caged_God","The_Sentry","Matsya","Nazirs_Judgement","Collapsing_Horizon",
    "The_Wicked_Quill","Chaos_Bolt","Sanguine_Diviner","Bone_Blast","Lifesprig",
    "Mana_Drain","Adonias_Ego","Power_Siphon","Pinnacle_of_Power","Enezuns_Charge",
    "Volatile_Dead","Cursecarver","Decompose","Dusk_Vigil","Firebolt",
    "Ember_Fusillade","Taryns_Shiver","Freezing_Shards","Earthbound","Lightning_Bolt",
    "Spark","The_Searing_Touch","Solar_Orb","Sire_of_Shards","Sigil_of_Power",
    "The_Burden_of_Shadows","The_Unborn_Lich","Feast_of_Flesh","The_Whispering_Ice",
    "Heart_of_Ice","Icestorm","Atziris_Rule","Mirror_of_Refraction","Widowhail",
    "Quill_Rain","Ironbound","Splinterheart","Doomfletch","Deaths_Harp",
    "Slivertongue","Fairgraves_Curse","Phantasmal_Arrow","Lioneyes_Glare","Mist_Whisper",
    "Rampart_Raptor","Double_Vision","Gemini_Surge","The_Dark_Defiler","Skeletal_Warrior",
    "Font_of_Power","Malice","Sacred_Flame","Purity_of_Fire","Guiding_Palm_of_the_Heart",
    "Guiding_Palm_of_the_Eye","Purity_of_Ice","Guiding_Palm_of_the_Mind","Purity_of_Lightning",
    "Palm_of_the_Dreamer","Impurity","Amor_Mandragora","Hyssegs_Claw","Cackling_Companions",
    "The_Flesh_Poppet","Seeing_Stars","Voltaxic_Rift","The_Last_Lament","Requiem",
    "Atziris_Contempt","Shattering_Spite","Fury_of_the_King","Molten_Crash",
    "Bramblejack","Blackbraid","Edyrns_Tusks","The_Road_Warrior","Titanrot_Cataphract",
    "Wandering_Reliquary","Kingsguard","Greeds_Embrace","The_Brass_Dome","Kaoms_Heart",
    "Bristleboar","Foxshade","Ashrend","Sands_of_Silk","Blink",
    "Briskwrap","Dustbloom","The_Rat_Cage","Quatls_Molt","Queen_of_the_Forest",
    "Yriels_Fostering","Hyrris_Ire","Ghostwrithe","Bitterbloom","The_Black_Doubt",
    "Necromantle","Cloak_of_Flame","Temporalis","Prayers_for_Rain","Tetzlapokals_Desire",
    "The_Covenant","Life_Remnants","Gloamgown","Vis_Mortis","Cloak_of_Defiance",
    "Silks_of_Veneration","Coat_of_Red","The_Barrow_Dweller","Irongrasp","Pariahs_Embrace",
    "Belly_of_the_Beast","Pragmatism","Doryanis_Prototype","Widows_Reign","Perfidy",
    "Lightning_Coil","Valakos_Charge","The_Coming_Calamity","Herald_of_Ash","Herald_of_Ice",
    "Herald_of_Thunder","Enfolding_Dawn","Icetomb","Reverie","Soul_Mantle",
    "The_Mutable_Star","Waveshaper","Couture_of_Crimson","Sacrosanctum","Apron_of_Emiran",
    "Gloomform","Sierran_Inheritance","The_Dancing_Mirage","Redflare_Conduit","Zerphis_Serape",
    "Cospris_Will","Withering_Presence","Wings_of_Caelyn","Horns_of_Bynden","Ezomyte_Peak",
    "Black_Sun_Crest","Thrillsteel","Deidbell","Corona_of_the_Red_Sun","Blood_Price",
    "Innsmouth","Goldrim","Radiant_Grief","Elevore","Constricting_Command",
    "The_Black_Insignia","Starkonjas_Head","Heatshiver","Myris_Uxor","Alphas_Howl",
    "Crown_of_Thorns","The_Devouring_Diadem","Visage_of_Ayah","Sandstorm_Visage",
    "Mask_of_the_Stitched_Demon","Atziris_Disdain","Crown_of_Eyes","Scolds_Bridle",
    "Indigon","Greymake","Erians_Cobble","Ironride","The_Smiling_Knight",
    "The_Vile_Knight","Assailum","The_Bringer_of_Rain","Crown_of_the_Victor","Bronzebeard",
    "Crown_of_the_Pale_King","Veil_of_the_Night","Cornathaum","Keeper_of_the_Arc",
    "The_Hollow_Mask","Mask_of_the_Sanguimancer","Leer_Cast","Atsaks_Sight","The_Vertex",
    "Glimpse_of_Chaos","The_Three_Dragons","Mind_of_the_Council","Treefingers",
    "Lochtonial_Caress","Dreadfist","Atziris_Acuity","Hateforge","Empires_Grasp",
    "Northpaw","Grip_of_Winter","Idle_Hands","Snakebite","Maligaros_Virtuosity",
    "Painters_Servant","Candlemaker","Doedres_Tenure","Kitokos_Current","Demon_Stitcher",
    "Nightscale","Leopolds_Applause","Jarngreipr","Aurseize","Deathblow",
    "Valakos_Vice","Aerisvanes_Wings","Death_Articulated","Gravebind","Shackles_of_the_Wretched",
    "Blueflame_Bracers","The_Prisoners_Manacles","Plaguefinger","Killjoy","Blessed_Bonds",
    "Hand_of_Wisdom_and_Action","Essentia_Sanguis","Thunderfist","Crackling_Palm",
    "Legionstride","Corpsewade","The_Infinite_Pursuit","Trampletoe","Birth_of_Fury",
    "Briarpatch","Gamblesprint","Bushwhack","Luminous_Pace","Wanderlust",
    "Bones_of_Ullr","Wondertrap","Windscream","The_Knight-errant","Darkray_Vectors",
    "Oberns_Bastion","Shankgonne","Black_Powder_Blitz","Wake_of_Destruction","Ghostmarch",
    "Powertread","Beetlebite","Dionadair","Raise_Shield","Wulfsbane",
    "Doomgate","Window_to_Paradise","Lycosidae","Redblade_Banner","Svalinn",
    "Cast_on_Block","Chernobogs_Pillar","Arvils_Wheel","Feathered_Fortress","Alkem_Eira",
    "Oaksworn","Saffells_Frame","Crest_of_Ardura","Mahuxotls_Machination","Rise_of_the_Phoenix",
    "Dunkelhalt","Parry","Nocturne","Rondel_de_Ezo","Bloodbarrier",
    "Kaltenhalt","Silverthorne","Calgyras_Arc","Sunsplinter","Deathrattle",
    "Threaded_Light","Effigy_of_Cruelty","Carrion_Call","Serpents_Lesson","The_Eternal_Spark",
    "Apeps_Supremacy","Tabula_Rasa","Skin_of_the_Loyal","Morior_Invictus","Atziris_Splendour",
    "Solus_Ipse","Sine_Aequo","Ab_Aeterno","Demigods_Virtue","Volls_Protector",
    "Atziris_Step","The_Surrender","Prism_Guardian","Rathpith_Globe","Heroic_Tragedy",
    "Undying_Hate","Grand_Spectrum","Megalomaniac","From_Nothing","Controlled_Metamorphosis",
    "Prism_of_Belief","The_Adorned","Heart_of_the_Well","Flesh_Crucible","Against_the_Darkness",
    "The_Peacemakers_Draught","The_Desperate_Alliance","The_Changing_Seasons",
    "The_Burden_of_Leadership","The_Last_Flame","Asphyxias_Wrath","Blackgleam",
    "The_Lethal_Draw","Rearguard","Murkshaft","Bursting_Fen_Toad","Cadiros_Gambit",
    "Drillneck","Beyond_Reach","Igniferis","Idol_of_Uldurn","The_Everlasting_Gaze",
    "Ungils_Harmony","Revered_Resin","Carnage_Heart","Xophs_Blood","Surefooted_Sigil",
    "Choir_of_the_Storm","Defiance_of_Destiny","Ligurium_Talisman","The_Pandemonius",
    "Stone_of_Lazhwar","Rondel_of_Fragility","The_Anvil","Yoke_of_Suffering","Astramentis",
    "Fixation_of_Yix","Strugglescream","Hinekoras_Sight","Future-Past","Beacon_of_Azis",
    "Fireflower","Eye_of_Chayula","Serpents_Egg","Blackheart","Icefang_Orbit",
    "Prized_Pain","Venopuncture","Doedres_Damning","Glowswarm","Seed_of_Cataclysm",
    "Cracklecreep","Blistering_Bond","Polcirkeln","Dream_Fragments","Whisper_of_the_Brotherhood",
    "The_Burrower","Call_of_the_Brotherhood","Levinstone","Mings_Heart","Original_Sin",
    "Blackflame","Vigilant_View","Death_Rush","Thiefs_Torment","Evergrasping_Ring",
    "Snakepit","Heartbound_Loop","Gifts_from_Above","Perandus_Seal","Andvarius",
    "Ventors_Gamble","Bursting_Decay","Grip_of_Kulemak","Meginords_Girdle","Midnight_Braid",
    "Keelhaul","Umbilicus_Immortalis","Birthright_Buckle","Byrnabas","The_Gnashing_Sash",
    "Soul_Tether","Goregirdle","Ryslathas_Coil","Cowards_Legacy","Bijouborne",
    "Cast_on_Charm_Use","Waistgate","Headhunter","Zerphis_Genesis","Ingenuity",
    "Shavronnes_Satchel","Darkness_Enthroned","Blood_of_the_Warrior","Olroths_Resolve",
    "Laviangas_Spirits","Melting_Maelstrom","Nascent_Hope","Sanguis_Heroum","Arakaalis_Gift",
    "Beiras_Anguish","The_Black_Cat","For_Utopia","The_Fall_of_the_Axe","Ngamahus_Chosen",
    "Breath_of_the_Mountains","Valakos_Roar","Forsaken_Bangle","Rite_of_Passage",
    "Kalandras_Touch","Sekhemas_Resolve","Wraeclast_Besieged","Forgotten_By_Time",
    "Clear_Skies","Freedom_of_Faith","The_Grand_Project","Visions_of_Paradise",
    "Season_of_the_Hunt","Cruel_Hegemony","Unforeseen_Consequences",
]


def clean(el) -> str:
    """Collapse whitespace in element text."""
    return " ".join(el.get_text(" ", strip=True).split())


def extract_item(html: str, slug: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    popup = soup.find("div", class_="newItemPopup")
    if not popup:
        popup = soup.find("div", class_="UniquePopup")

    item_name = ""
    base_type = ""
    item_class_line = ""  # first property = item class (e.g. "Spears")
    properties = []       # base stats (damage, APS, etc.)
    requirements = ""
    implicit_mods = []
    explicit_mods = []
    flavor = ""

    if popup:
        # Header: itemName + typeLine
        name_el = popup.find(class_="itemName")
        if name_el:
            item_name = clean(name_el)
        base_el = popup.find(class_="typeLine")
        if base_el:
            base_type = clean(base_el)

        # Stats div children
        stats_div = popup.find("div", class_="Stats")
        if stats_div:
            prop_list = []
            for child in stats_div.children:
                if not hasattr(child, "name") or not child.name:
                    continue
                cls = child.get("class", [])
                txt = clean(child)
                if not txt:
                    continue
                if "property" in cls:
                    prop_list.append(txt)
                elif "requirements" in cls:
                    requirements = txt
                elif "implicitMod" in cls:
                    implicit_mods.append(txt)
                elif "explicitMod" in cls:
                    explicit_mods.append(txt)
                elif "FlavourText" in cls or "flavourText" in cls:
                    flavor = txt

            # First property is item class (e.g. "Spears", "Bows", "Body Armour")
            if prop_list:
                item_class_line = prop_list[0]
                properties = prop_list[1:]

    if not item_name:
        title_el = soup.find("title")
        item_name = title_el.get_text(strip=True).split(" - ")[0] if title_el else unquote(slug.replace("_", " "))

    # Build markdown
    source_url = BASE_URL + slug
    md_lines = [
        "---",
        f"source_url: {source_url}",
        f"clipped: {TODAY}",
        f"patch: {PATCH}",
        "status: raw",
        "---",
        "",
        f"# {item_name}",
        "",
    ]

    if base_type:
        md_lines.append(f"**Base:** {base_type}")
    if item_class_line:
        md_lines.append(f"**Class:** {item_class_line}")
    if base_type or item_class_line:
        md_lines.append("")

    if properties:
        md_lines.append("## Base Stats")
        md_lines.append("")
        for p in properties:
            md_lines.append(p)
        md_lines.append("")

    if requirements:
        md_lines.append(f"**{requirements}**")
        md_lines.append("")

    if implicit_mods:
        md_lines.append("## Implicit")
        md_lines.append("")
        for m in implicit_mods:
            md_lines.append(f"- {m}")
        md_lines.append("")

    if explicit_mods:
        md_lines.append("## Modifiers")
        md_lines.append("")
        for m in explicit_mods:
            md_lines.append(f"- {m}")
        md_lines.append("")

    if flavor:
        md_lines.append("## Flavour")
        md_lines.append("")
        md_lines.append(f"> {flavor}")
        md_lines.append("")

    return "\n".join(md_lines)


def fetch_slug(session: requests.Session, slug: str) -> bool:
    # Filename uses decoded slug
    filename = unquote(slug).replace("/", "_") + ".md"
    out_path = os.path.join(OUT_DIR, filename)

    if os.path.exists(out_path):
        return True  # already downloaded

    url = BASE_URL + slug
    try:
        resp = session.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            print(f"  SKIP {slug} — HTTP {resp.status_code}")
            return False
        content = extract_item(resp.text, slug)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  ERROR {slug}: {e}")
        return False


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    session = requests.Session()

    total = len(SLUGS)
    ok = 0
    skip = 0
    err = 0

    for i, slug in enumerate(SLUGS, 1):
        filename = unquote(slug).replace("/", "_") + ".md"
        if os.path.exists(os.path.join(OUT_DIR, filename)):
            skip += 1
            if i % 50 == 0:
                print(f"[{i}/{total}] {ok} done, {skip} cached, {err} errors")
            continue

        print(f"[{i}/{total}] {slug}", end=" ... ", flush=True)
        success = fetch_slug(session, slug)
        if success:
            ok += 1
            print("OK")
        else:
            err += 1

        # Polite delay between requests
        time.sleep(0.3)

    print(f"\nDone: {ok} fetched, {skip} already existed, {err} errors")


if __name__ == "__main__":
    main()
