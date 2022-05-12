#!/usr/bin/env python
# coding: utf-8

import string


charmap = {
    "hi_IN": [u"ँ", u"ं", u"ः", u"ऄ", u"अ", u"आ", u"इ", u"ई", u"उ", u"ऊ", u"ऋ",
              u"ऌ", u"ऍ", u"ऎ", u"ए", u"ऐ", u"ऑ", u"ऒ", u"ओ", u"औ", u"क", u"ख",
              u"ग", u"घ", u"ङ", u"च", u"छ", u"ज", u"झ", u"ञ", u"ट", u"ठ", u"ड",
              u"ढ", u"ण", u"त", u"थ", u"द", u"ध", u"न", u"ऩ", u"प", u"फ", u"ब",
              u"भ", u"म", u"य", u"र", u"ऱ", u"ल", u"ळ", u"ऴ", u"व", u"श", u"ष",
              u"स", u"ह", u"ऺ", u"ऻ", u"़", u"ऽ", u"ा", u"ि", u"ी", u"ु", u"ू",
              u"ृ", u"ॄ", u"ॅ", u"ॆ", u"े", u"ै", u"ॉ", u"ॊ", u"ो", u"ौ", u"्",
              u"ॎ", u"ॏ", u"ॐ", u"॑", u"॒", u"॓", u"॔", u"ॕ", u"ॖ", u"ॗ", u"क़",
              u"ख़", u"ग़", u"ज़", u"ड़", u"ढ़", u"फ़", u"य़", u"ॠ", u"ॡ", u"ॢ", u"ॣ",
              u"।", u"॥", u"०", u"१", u"२", u"३", u"४", u"५", u"६", u"७", u"८",
              u"९", u"॰", u"ॱ", u"ॲ", u"ॳ", u"ॴ", u"ॵ", u"ॶ", u"ॷ", u"ॸ", u"ॹ",
              u"ॺ", u"ॻ", u"ॼ", u"ॽ", u"ॾ", u"ॿ"],
    "bn_IN": [u"ঁ", u"ং", u"ঃ", u"঄", u"অ", u"আ", u"ই", u"ঈ", u"উ", u"ঊ", u"ঋ",
              u"ঌ", u"঍", u"঎", u"এ", u"ঐ", u"঑", u"঒", u"ও", u"ঔ", u"ক", u"খ",
              u"গ", u"ঘ", u"ঙ", u"চ", u"ছ", u"জ", u"ঝ", u"ঞ", u"ট", u"ঠ", u"ড",
              u"ঢ", u"ণ", u"ত", u"থ", u"দ", u"ধ", u"ন", u"঩", u"প", u"ফ", u"ব",
              u"ভ", u"ম", u"য", u"র", u"঱", u"ল", u"঳", u"঴", u"঵", u"শ", u"ষ",
              u"স", u"হ", u"঺", u"঻", u"়", u"ঽ", u"া", u"ি", u"ী", u"ু", u"ূ",
              u"ৃ", u"ৄ", u"৅", u"৆", u"ে", u"ৈ", u"৉", u"৊", u"ো", u"ৌ",
              u"্", u"ৎ", u"৏", u"৐", u"৑", u"৒", u"৓", u"৔", u"৕", u"৖", u"ৗ",
              u"৘", u"৙", u"৚", u"৛", u"ড়", u"ঢ়", u"৞", u"য়", u"ৠ", u"ৡ", u"ৢ",
              u"ৣ", u"৤", u"৥", u"০", u"১", u"২", u"৩", u"৪", u"৫", u"৬", u"৭",
              u"৮", u"৯", u"ৰ", u"ৱ", u"৲", u"৳", u"৴", u"৵", u"৶", u"৷", u"৸",
              u"৹", u"৺", u"৻", u"ৼ", u"৽", u"৾", u"৿"],
    "pa_IN": [u"ਁ", u"ਂ", u"ਃ", u"਄", u"ਅ", u"ਆ", u"ਇ", u"ਈ", u"ਉ", u"ਊ", u"਋",
              u"਌", u"਍", u"਎", u"ਏ", u"ਐ", u"਑", u"਒", u"ਓ", u"ਔ", u"ਕ", u"ਖ",
              u"ਗ", u"ਘ", u"ਙ", u"ਚ", u"ਛ", u"ਜ", u"ਝ", u"ਞ", u"ਟ", u"ਠ", u"ਡ",
              u"ਢ", u"ਣ", u"ਤ", u"ਥ", u"ਦ", u"ਧ", u"ਨ", u"਩", u"ਪ", u"ਫ", u"ਬ",
              u"ਭ", u"ਮ", u"ਯ", u"ਰ", u"਱", u"ਲ", u"ਲ਼", u"਴", u"ਵ", u"ਸ਼", u"਷",
              u"ਸ", u"ਹ", u"਺", u"਻", u"਼", u"਽", u"ਾ", u"ਿ", u"ੀ", u"ੁ", u"ੂ",
              u"੃", u"੄", u"੅", u"੆", u"ੇ", u"ੈ", u"੉", u"੊", u"ੋ", u"ੌ", u"੍",
              u"੎", u"੏", u"੐", u"ੑ", u"੒", u"੓", u"੔", u"੕", u"੖", u"੗", u"੘",
              u"ਖ਼", u"ਗ਼", u"ਜ਼", u"ੜ", u"੝", u"ਫ਼", u"੟", u"੠", u"੡", u"੢", u"੣",
              u"੤", u"੥", u"੦", u"੧", u"੨", u"੩", u"੪", u"੫", u"੬", u"੭", u"੮",
              u"੯", u"ੰ", u"ੱ", u"ੲ", u"ੳ", u"ੴ", u"ੵ", u"੶", u"੷", u"੸", u"੹",
              u"੺", u"੻", u"੼", u"੽", u"੾", u"੿"],
    "gu_IN": [u"ઁ", u"ં", u"ઃ", u"઄", u"અ", u"આ", u"ઇ", u"ઈ", u"ઉ", u"ઊ", u"ઋ",
              u"ઌ", u"ઍ", u"઎", u"એ", u"ઐ", u"ઑ", u"઒", u"ઓ", u"ઔ", u"ક", u"ખ",
              u"ગ", u"ઘ", u"ઙ", u"ચ", u"છ", u"જ", u"ઝ", u"ઞ", u"ટ", u"ઠ", u"ડ",
              u"ઢ", u"ણ", u"ત", u"થ", u"દ", u"ધ", u"ન", u"઩", u"પ", u"ફ", u"બ",
              u"ભ", u"મ", u"ય", u"ર", u"઱", u"લ", u"ળ", u"઴", u"વ", u"શ", u"ષ",
              u"સ", u"હ", u"઺", u"઻", u"઼", u"ઽ", u"ા", u"િ", u"ી", u"ુ", u"ૂ",
              u"ૃ", u"ૄ", u"ૅ", u"૆", u"ે", u"ૈ", u"ૉ", u"૊", u"ો", u"ૌ", u"્",
              u"૎", u"૏", u"ૐ", u"૑", u"૒", u"૓", u"૔", u"૕", u"૖", u"૗", u"૘",
              u"૙", u"૚", u"૛", u"૜", u"૝", u"૞", u"૟", u"ૠ", u"ૡ", u"ૢ", u"ૣ",
              u"૤", u"૥", u"૦", u"૧", u"૨", u"૩", u"૪", u"૫", u"૬", u"૭", u"૮",
              u"૯", u"૰", u"૱", u"૲", u"૳", u"૴", u"૵", u"૶", u"૷", u"૸", u"ૹ",
              u"ૺ", u"ૻ", u"ૼ", u"૽", u"૾", u"૿"],
    "or_IN": [u"ଁ", u"ଂ", u"ଃ", u"଄", u"ଅ", u"ଆ", u"ଇ", u"ଈ", u"ଉ", u"ଊ", u"ଋ",
              u"ଌ", u"଍", u"଎", u"ଏ", u"ଐ", u"଑", u"଒", u"ଓ", u"ଔ", u"କ", u"ଖ",
              u"ଗ", u"ଘ", u"ଙ", u"ଚ", u"ଛ", u"ଜ", u"ଝ", u"ଞ", u"ଟ", u"ଠ", u"ଡ",
              u"ଢ", u"ଣ", u"ତ", u"ଥ", u"ଦ", u"ଧ", u"ନ", u"଩", u"ପ", u"ଫ", u"ବ",
              u"ଭ", u"ମ", u"ଯ", u"ର", u"଱", u"ଲ", u"ଳ", u"଴", u"ଵ", u"ଶ", u"ଷ",
              u"ସ", u"ହ", u"଺", u"଻", u"଼", u"ଽ", u"ା", u"ି", u"ୀ", u"ୁ", u"ୂ",
              u"ୃ", u"ୄ", u"୅", u"୆", u"େ", u"ୈ", u"୉", u"୊", u"ୋ", u"ୌ", u"୍",
              u"୎", u"୏", u"୐", u"୑", u"୒", u"୓", u"୔", u"୕", u"ୖ", u"ୗ", u"୘",
              u"୙", u"୚", u"୛", u"ଡ଼", u"ଢ଼", u"୞", u"ୟ", u"ୠ", u"ୡ", u"ୢ", u"ୣ",
              u"୤", u"୥", u"୦", u"୧", u"୨", u"୩", u"୪", u"୫", u"୬", u"୭", u"୮",
              u"୯", u"୰", u"ୱ", u"୲", u"୳", u"୴", u"୵", u"୶", u"୷", u"୸", u"୹",
              u"୺", u"୻", u"୼", u"୽", u"୾", u"୿"],
    "ta_IN": [u"஁", u"ஂ", u"ஃ", u"஄", u"அ", u"ஆ", u"இ", u"ஈ", u"உ", u"ஊ", u"஋",
              u"஌", u"஍", u"எ", u"ஏ", u"ஐ", u"஑", u"ஒ", u"ஓ", u"ஔ", u"க", u"஖",
              u"஗", u"஘", u"ங", u"ச", u"஛", u"ஜ", u"஝", u"ஞ", u"ட", u"஠", u"஡",
              u"஢", u"ண", u"த", u"஥", u"஦", u"஧", u"ந", u"ன", u"ப", u"஫", u"஬",
              u"஭", u"ம", u"ய", u"ர", u"ற", u"ல", u"ள", u"ழ", u"வ", u"ஶ", u"ஷ",
              u"ஸ", u"ஹ", u"஺", u"஻", u"஼", u"஽", u"ா", u"ி", u"ீ", u"ு", u"ூ",
              u"௃", u"௄", u"௅", u"ெ", u"ே", u"ை", u"௉", u"ொ", u"ோ", u"ௌ", u"்",
              u"௎", u"௏", u"ௐ", u"௑", u"௒", u"௓", u"௔", u"௕", u"௖", u"ௗ", u"௘",
              u"௙", u"௚", u"௛", u"௜", u"௝", u"௞", u"௟", u"௠", u"௡", u"௢", u"௣",
              u"௤", u"௥", u"௦", u"௧", u"௨", u"௩", u"௪", u"௫", u"௬", u"௭", u"௮",
              u"௯", u"௰", u"௱", u"௲", u"௳", u"௴", u"௵", u"௶", u"௷", u"௸", u"௹",
              u"௺", u"௻", u"௼", u"௽", u"௾", u"௿"],
    "te_IN": [u"ఁ", u"ం", u"ః", u"ఄ", u"అ", u"ఆ", u"ఇ", u"ఈ", u"ఉ", u"ఊ", u"ఋ",
              u"ఌ", u"఍", u"ఎ", u"ఏ", u"ఐ", u"఑", u"ఒ", u"ఓ", u"ఔ", u"క", u"ఖ",
              u"గ", u"ఘ", u"ఙ", u"చ", u"ఛ", u"జ", u"ఝ", u"ఞ", u"ట", u"ఠ", u"డ",
              u"ఢ", u"ణ", u"త", u"థ", u"ద", u"ధ", u"న", u"఩", u"ప", u"ఫ", u"బ",
              u"భ", u"మ", u"య", u"ర", u"ఱ", u"ల", u"ళ", u"ఴ", u"వ", u"శ", u"ష",
              u"స", u"హ", u"఺", u"఻", u"఼", u"ఽ", u"ా", u"ి", u"ీ", u"ు", u"ూ",
              u"ృ", u"ౄ", u"౅", u"ె", u"ే", u"ై", u"౉", u"ొ", u"ో", u"ౌ", u"్",
              u"౎", u"౏", u"౐", u"౑", u"౒", u"౓", u"౔", u"ౕ", u"ౖ", u"౗", u"ౘ",
              u"ౙ", u"ౚ", u"౛", u"౜", u"ౝ", u"౞", u"౟", u"ౠ", u"ౡ", u"ౢ", u"ౣ",
              u"౤", u"౥", u"౦", u"౧", u"౨", u"౩", u"౪", u"౫", u"౬", u"౭", u"౮",
              u"౯", u"౰", u"౱", u"౲", u"౳", u"౴", u"౵", u"౶", u"౷", u"౸", u"౹",
              u"౺", u"౻", u"౼", u"౽", u"౾", u"౿"],
    "kn_IN": [u"ಁ", u"ಂ", u"ಃ", u"಄", u"ಅ", u"ಆ", u"ಇ", u"ಈ", u"ಉ", u"ಊ", u"ಋ",
              u"ಌ", u"಍", u"ಎ", u"ಏ", u"ಐ", u"಑", u"ಒ", u"ಓ", u"ಔ", u"ಕ", u"ಖ",
              u"ಗ", u"ಘ", u"ಙ", u"ಚ", u"ಛ", u"ಜ", u"ಝ", u"ಞ", u"ಟ", u"ಠ", u"ಡ",
              u"ಢ", u"ಣ", u"ತ", u"ಥ", u"ದ", u"ಧ", u"ನ", u"಩", u"ಪ", u"ಫ", u"ಬ",
              u"ಭ", u"ಮ", u"ಯ", u"ರ", u"ಱ", u"ಲ", u"ಳ", u"಴", u"ವ", u"ಶ", u"ಷ",
              u"ಸ", u"ಹ", u"಺", u"಻", u"಼", u"ಽ", u"ಾ", u"ಿ", u"ೀ", u"ು", u"ೂ",
              u"ೃ", u"ೄ", u"೅", u"ೆ", u"ೇ", u"ೈ", u"೉", u"ೊ", u"ೋ", u"ೌ", u"್",
              u"೎", u"೏", u"೐", u"೑", u"೒", u"೓", u"೔", u"ೕ", u"ೖ", u"೗", u"೘",
              u"೙", u"೚", u"೛", u"೜", u"ೝ", u"ೞ", u"೟", u"ೠ", u"ೡ", u"ೢ", u"ೣ",
              u"೤", u"೥", u"೦", u"೧", u"೨", u"೩", u"೪", u"೫", u"೬", u"೭", u"೮",
              u"೯", u"೰", u"ೱ", u"ೲ", u"ೳ", u"೴", u"೵", u"೶", u"೷", u"೸", u"೹",
              u"೺", u"೻", u"೼", u"೽", u"೾", u"೿"],
    "ml_IN": [u"ഁ", u"ം", u"ഃ", u"ഄ", u"അ", u"ആ", u"ഇ", u"ഈ", u"ഉ", u"ഊ", u"ഋ",
              u"ഌ", u"഍", u"എ", u"ഏ", u"ഐ", u"഑", u"ഒ", u"ഓ", u"ഔ", u"ക", u"ഖ",
              u"ഗ", u"ഘ", u"ങ", u"ച", u"ഛ", u"ജ", u"ഝ", u"ഞ", u"ട", u"ഠ", u"ഡ",
              u"ഢ", u"ണ", u"ത", u"ഥ", u"ദ", u"ധ", u"ന", u"ഩ", u"പ", u"ഫ", u"ബ",
              u"ഭ", u"മ", u"യ", u"ര", u"റ", u"ല", u"ള", u"ഴ", u"വ", u"ശ", u"ഷ",
              u"സ", u"ഹ", u"ഺ", u"഻", u"഼", u"ഽ", u"ാ", u"ി", u"ീ", u"ു", u"ൂ",
              u"ൃ", u"ൄ", u"൅", u"െ", u"േ", u"ൈ", u"൉", u"ൊ", u"ോ", u"ൌ", u"്",
              u"ൎ", u"൏", u"൐", u"൑", u"൒", u"൓", u"ൔ", u"ൕ", u"ൖ", u"ൗ", u"൘",
              u"൙", u"൚", u"൛", u"൜", u"൝", u"൞", u"ൟ", u"ൠ", u"ൡ", u"ൢ", u"ൣ",
              u"൤", u"൥", u"൦", u"൧", u"൨", u"൩", u"൪", u"൫", u"൬", u"൭", u"൮",
              u"൯", u"൰", u"൱", u"൲", u"൳", u"൴", u"൵", u"൶", u"൷", u"൸", u"൹",
              u"ൺ", u"ൻ", u"ർ", u"ൽ", u"ൾ", u"ൿ"],
    "en_US": [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"k",
              u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v",
              u"w", u"x", u"y", u"z"],
    "ISO15919": ["m̐", "ṁ", "ḥ", "", "a", "ā", "i", "ī", "u", "ū", "ṛ", "ḷ",
                 "ê", "e", "ē", "ai", "ô", "o", "ō", "au", "ka", "kha", "ga",
                 "gha", "ṅa", "ca", "cha", "ja", "jha", "ña", "ṭa", "ṭha",
                 "ḍa", "ḍha", "ṇa", "ta", "tha", "da", "dha", "na", "ṉa",
                 "pa", "pha", "ba", "bha", "ma", "ya", "ra", "ṟa", "la", "ḷa",
                 "ḻa", "va", "śa", "ṣa", "sa", "ha", "", "", "", "'", "ā", "i",
                 "ī", "u", "ū", "ṛ", "ṝ", "ê", "e", "ē", "ai", "ô", "o", "ō",
                 "au", "", "", "", "oṃ", "", "", "", "", "", "", "", "qa",
                 "ḵẖa", "ġ", "za", "ṛa", "ṛha", "fa", "ẏa", "ṝ", "ḹ", "ḷ",
                 "ḹ", ".", "..", "0", "1", "2", "3", "4", "5", "6", "7", "8",
                 "9", "…", "", "", "", "", "", "", "", "", "", "", "", "", "",
                 "", "", "", ""],
    "IPA": ["m", "m", "", "", "ə", "aː", "i", "iː", "u", "uː", "r̩", "l̩", "æ",
            "e", "eː", "ɛː", "ɔ", "o", "oː", "ow", "kə", "kʰə", "gə", "gʱə",
            "ŋə", "ʧə", "ʧʰə", "ʤə", "ʤʱə", "ɲə", "ʈə", "ʈʰə", "ɖə", "ɖʱə",
            "ɳə", "t̪ə", "t̪ʰə", "d̪ə", "d̪ʱə", "n̪ə", "nə", "pə", "pʰə", "bə",
            "bʱə", "mə", "jə", "ɾə", "rə", "lə", "ɭə", "ɻə", "ʋə", "ɕə", "ʂə",
            "sə", "ɦə", "", "", "", "ഽ", "aː", "i", "iː", "u", "uː", "r̩",
            "l̩", "e", "eː", "ɛː", "ɔ", "o", "oː", "ow", "", "", "", "", "",
            "", "", "", "", "", "ow", "", "", "", "", "", "", "", "", "r̩ː",
            "l̩ː", "", "", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8",
            "9", "൰", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            ""]
}


lang_bases = {
    'en_US': 0, 'en_IN': 0, 'hi_IN': 0x0901, 'bn_IN': 0x0981,
    'pa_IN': 0x0A01, 'gu_IN': 0x0A81, 'or_IN': 0x0B01, 'ta_IN': 0x0B81,
    'te_IN': 0x0C01, 'kn_IN': 0x0C81, 'ml_IN': 0x0D01
}


def detect_lang(text):
    """
    Detect the language of the given text using the unicode range.
    This function can take a chunk of text and return a dictionary
    containing word-language key-value pairs.
    """
    words = text.split(" ")
    word_count = len(words)
    word_iter = 0
    word = ""
    result_dict = dict()
    while word_iter < word_count:
        word = words[word_iter]
        if(word):
            orig_word = word
            # remove the punctuations
            for punct in string.punctuation:
                word = word.replace(punct, " ")
            length = len(word)
            index = 0
            # scan left to write, skip any punctuations,
            # the detection stops in the first match itself.
            while index < length:
                letter = word[index]
                #if not letter.isalpha():
                 #   index = index + 1
                  #  continue
                if ((ord(letter) >= 0x0D00) & (ord(letter) <= 0x0D7F)):
                    result_dict[orig_word] = "ml_IN"
                    break
                if ((ord(letter) >= 0x0980) & (ord(letter) <= 0x09FF)):
                    result_dict[orig_word] = "bn_IN"
                    break
                if ((ord(letter) >= 0x0900) & (ord(letter) <= 0x097F)):
                    result_dict[orig_word] = "hi_IN"
                    #print "here"
                    break
                if ((ord(letter) >= 0x0A80) & (ord(letter) <= 0x0AFF)):
                    result_dict[orig_word] = "gu_IN"
                    break
                if ((ord(letter) >= 0x0A00) & (ord(letter) <= 0x0A7F)):
                    result_dict[orig_word] = "pa_IN"
                    break
                if ((ord(letter) >= 0x0C80) & (ord(letter) <= 0x0CFF)):
                    result_dict[orig_word] = "kn_IN"
                    break
                if ((ord(letter) >= 0x0B00) & (ord(letter) <= 0x0B7F)):
                    result_dict[orig_word] = "or_IN"
                    break
                if ((ord(letter) >= 0x0B80) & (ord(letter) <= 0x0BFF)):
                    result_dict[orig_word] = "ta_IN"
                    break
                if ((ord(letter) >= 0x0C00) & (ord(letter) <= 0x0C7F)):
                    result_dict[orig_word] = "te_IN"
                    break
                if ((letter <= u'z')):  # this is fallback case.
                    #result_dict[orig_word] = "en_US"
                    break
                index = index + 1
        word_iter = word_iter + 1
    return result_dict


def transliterate_iso15919( word, src_language):
        tx_str = ""
        index = 0
        word_length = len(word)
        for chr in word:
            index += 1
            offset = ord(chr) - lang_bases[src_language]
            #76 is the virama offset for all indian languages from its base
            if offset >= 61 and offset <= 76:
                tx_str = tx_str[:-1]  # remove the last 'a'
            if offset > 0 and offset <= 128:
                tx_str = tx_str + charmap["ISO15919"][offset]
            #delete the inherent 'a' at the end of the word from hindi
            if tx_str[-1:] == 'a' and (src_language == "hi_IN"
                                       or src_language == "gu_IN"
                                       or src_language == "bn_IN"):
                if word_length == index and word_length > 1:  # if last letter
                    tx_str = tx_str[:-1]  # remove the last 'a'
        if tx_str == "":
            tx_str = wrd
        return tx_str # .decode("utf-8")
    

def transliterate_ipa( word, src_language):
        """
        Transliterate the given word in src_language to
        IPA - International Phonetical Alphabet notation.
        """
        tx_str = ""
        index = 0
        word_length = len(word)
        for chr in word:
            index += 1
            if ord(chr) < 255:  # ASCII characters + English
                tx_str += chr
                continue
            offset = ord(chr) - lang_bases[src_language]
            #76 is the virama offset for all indian languages from its base
            if offset >= 61 and offset <= 76:
                tx_str = tx_str[:-(len('ə'))]  # remove the last 'ə'
            if offset > 0 and offset <= 128:
                tx_str = tx_str + charmap["IPA"][offset]
            #delete the inherent 'a' at the end of the word from hindi
            if tx_str[-1:] == 'ə' and                (src_language == "hi_IN"
                or src_language == "gu_IN"
                or src_language == "bn_IN") and \
               (word_length == index
                and word_length > 1): tx_str = tx_str[:-(len('ə'))]
            # if last letter
            # remove the last 'a'
        return tx_str  #.decode("utf-8") # not needed in python3


def transliterate_indic_indic( word, src_lang, target_lang):
        """
            Transliterate from an Indian languge word
            to another indian language word
        """
        index = 0
        tx_str = ""
        #word = self.normalizer.normalize(word)
        if src_lang == "ml_IN" and target_lang != "ml_IN":
            word = word.replace(u"\u200C", u"")
            word = word.replace(u"\u200D", u"")
            #replace all samvruthokaram by u vowels
            word = word.replace(u"ു്", u"")

        for chr in word:
            index += 1
            if chr in string.punctuation or (ord(chr) <= 2304
                                             and ord(chr) >= 3071):
                tx_str = tx_str + chr
                continue
            offset = ord(chr) + getOffset(src_lang, target_lang)
            if(offset > 0):
                tx_str = tx_str + unichr(offset)
            #schwa deletion
            baseoffset = offset - lang_bases[target_lang]
            #76 : virama
            if (index == len(word) and baseoffset == 76
                    and (target_lang == "hi_IN"
                         or target_lang == "gu_IN"
                         or target_lang == "pa_IN"
                         or target_lang == "bn_IN")):
                #TODO Add more languages having schwa deletion characteristic
                tx_str = tx_str[:-(len(chr))]  # remove the last 'a'

            if target_lang == "ml_IN" and src_lang == "ta_IN":
                tx_str = tx_str.replace(u"ഩ", u"ന")

            if target_lang == "ta_IN":
                tx_str = tx_str.replace(u'\u0B96', u"க")
                tx_str = tx_str.replace(u'\u0B97', u"க")
                tx_str = tx_str.replace(u'\u0B98', u"க")
                tx_str = tx_str.replace(u'\u0B9B', u"ச")
                tx_str = tx_str.replace(u'\u0B9D', u"ச")
                tx_str = tx_str.replace(u'\u0BA0', u"ட")
                tx_str = tx_str.replace(u'\u0BA1', u"ட")
                tx_str = tx_str.replace(u'\u0BA2', u"ட")
                tx_str = tx_str.replace(u'\u0BA5', u"த")
                tx_str = tx_str.replace(u'\u0BA6', u"த")
                tx_str = tx_str.replace(u'\u0BA7', u"த")
                tx_str = tx_str.replace(u'\u0BAB', u"ப")
                tx_str = tx_str.replace(u'\u0BAC', u"ப")
                tx_str = tx_str.replace(u'\u0BAD', u"ப")
                tx_str = tx_str.replace(u'\u0BC3', u"ிரு")
                tx_str = tx_str.replace(u'ஂ', u'ம்')
        #If target is malayalam, we need to add the virama
        if ((target_lang == "ml_IN") and
            (src_lang == "hi_IN"
             or src_lang == "gu_IN"
             or src_lang == "pa_IN"
             or src_lang == "bn_IN") and tx_str[-1].isalpha()):
            tx_str = tx_str + u"്"
        return tx_str


def getOffset( src, target):
    src_id = 0
    target_id = 0
    try:
        src_id = lang_bases[src]
        target_id = lang_bases[target]
        return (target_id - src_id)
    except:
        return 0
    

def tokenize(text):
    words = text.split(" ")
    nSent=""
    for x in words:
        nWord=""
        first=True
        bet=False
        for c in x:
            if(len(detect_lang(c))==0 and first):
                nWord=nWord+c+" "
            else:
                if(len(detect_lang(c))==0):
                    nWord=nWord+" "+c
                    bet=True
                else:
                    if (bet):
                        nWord=nWord+" "+c
                        bet=False
                    else:
                        nWord=nWord+c
            first=False
        nSent=nSent+" "+nWord
    return nSent


def basic_cleaning(data):
    data = data.replace("[!]+",". ").replace("\.{2,}",".").replace('\u200c','').replace('\u200b','').replace('\xa0',' ').replace('\x7f',' ').replace('\ufeff','').replace('\.+"+','"').replace('["]+',"")
    data = data.replace("\.+'+","'").replace('\.+\s*-+',', ').replace("[:\?\t]+"," ").replace("[\n]+","\n").replace("[\r]+","")
    data = data.replace('&', '').replace('&nbsp;', '')
    data = data.replace('\,+', ',')
    data = ' '.join(data.split())
    data = data.strip()
    return data


def demo(text=None, lang='te_IN'):

    if not text and lang=='te_IN':
        text = u"హైదరాబాద్‌ సెంట్రల్‌ యూనివర్శిటీ ( హెచ్‌సియు ) covid-19 ఓ విద్యార్థి మృతి చెందారు. శంషాబాద్‌ ఔటర్‌ రింగ్‌రోడ్డుపై మంగళవారం ఉదయం కారు ప్రమాదం జరిగింది. ఈ ప్రమాదంలో యోగాల్‌ అనే విద్యార్థి మృతి చెందగా మరో ఇద్దరికి తీవ్ర గాయాలయ్యాయి. పోలీసులు కేసు నమోదు చేసి దర్యాప్తు చేస్తున్నారు."
    if not text and lang=='hi_IN':
        text = u"मीरा कहती हैं,\"पाकिस्तान में मैंने अपने बेटे का नाम भारत रखा था और बेटी का नाम भारती रखा था .फिर हम भारत आ गए . अब भारत में बात चल रही है कि हमें नागरिकता मिल सकती है , तो मैंने सोचा कि अपनी पोती का नाम \'नागरिकता \' रखती हूं . ये बच्ची होते ही नागरिकता की बात शुरू हो गई . क्या पता , इसी के भाग्य से हमें नागरिकता मिलने जा रही है ."

    cleaned_text = basic_cleaning(text)
    print('cleaned_text: ', cleaned_text)

    nSent = tokenize(cleaned_text)
    print('tokenized text: ', nSent)

    sent = []
    print('tokens list: ', nSent.split())

    for wrd in nSent.split():
        sent.append(transliterate_iso15919(wrd, lang))
    print('Transliteration:\n', ' '.join(sent))
