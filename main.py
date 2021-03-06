import time
import datetime
import webbrowser

import pyperclip
import pyautogui

AzkharAlsabah = [
"اللَّهُمَّ أنْتَ رَبِّي لا إلَهَ إلَّا أنْتَ، خَلَقْتَنِي وأنا عَبْدُكَ، وأنا علَى عَهْدِكَ ووَعْدِكَ ما اسْتَطَعْتُ، أعُوذُ بكَ مِن شَرِّ ما صَنَعْتُ، أبُوءُ لكَ بنِعْمَتِكَ عَلَيَّ، وأَبُوءُ لكَ بذَنْبِي فاغْفِرْ لِي، فإنَّه لا يَغْفِرُ الذُّنُوبَ إلَّا أنْت",
'أَصبَحْنا على فِطرةِ الإسلامِ، وعلى كَلِمةِ الإخلاصِ، وعلى دِينِ نَبيِّنا محمَّدٍ صلَّى اللهُ عليه وسلَّمَ، وعلى مِلَّةِ أبِينا إبراهيمَ، حَنيفًا مُسلِمًا، وما كان مِنَ المُشرِكينَ',
'سبحانَ اللَّهِ وبحمدِه لا قوَّةَ إلَّا باللَّهِ ما شاءَ اللَّهُ كانَ وما لم يشأ لم يَكن أعلمُ أنَّ اللَّهَ على كلِّ شيءٍ قديرٌ وأنَّ اللَّهَ قد أحاطَ بِكلِّ شيءٍ علمًا',
'قال رسول الله صلى الله عليه وسلم: (مَن قال: بسمِ اللهِ الذي لا يَضرُ مع اسمِه شيءٌ في الأرضِ ولا في السماءِ وهو السميعُ العليمِ، ثلاثُ مراتٍ، لم تصبْه فجأةُ بلاءٍ حتى يُصبحَ)',
'قال رسول الله صلى الله عليه وسلم: (مَن قالَ حينَ يصبحُ وحينَ يُمسي: سبحانَ اللَّهِ وبحمدِهِ مائةَ مرَّةٍ: لم يأتِ أحدٌ يومَ القيامةِ بأفضلَ ممَّا جاءَ بِهِ، إلَّا أحدٌ قالَ مثلَ ما قالَ، أو زادَ علَيهِ)',
'اللهمَّ إني أسألُك العفوَ والعافيةَ، في الدنيا والآخرةِ، اللهمَّ إني أسألُك العفوَ والعافيةَ، في دِيني ودنيايَ وأهلي ومالي، اللهمَّ استُرْ عوراتي، وآمِنْ روعاتي، واحفظني من بين يدي، ومن خلفي، وعن يميني، وعن شمالي، ومن فوقي، وأعوذُ بك أن أُغْتَالَ من تحتي',
'للَّهمَّ بِكَ أصبَحنا، وبِكَ أمسَينا، وبِكَ نحيا وبِكَ نموتُ وإليكَ المصيرُ',
'اللهمَّ إنِّي أعوذُ بك من الهمِّ والحزنِ، والعجزِ والكسلِ، والبُخلِ والجُبنِ، وضَلَعِ الدَّينِ، وغَلَبَةِ الرجالِ',
'اللَّهمَّ إنِّي أسألُكَ خيرَ هذا اليومِ فتحَه، ونصرَه، ونورَه، وبرَكتَه، وَهدايتَهُ، وأعوذُ بِكَ من شرِّ ما فيهِ وشرِّ ما بعدَه',
'اللَّهُمَّ إنِّي أسألُكَ العافيةَ في الدُّنيا والآخِرةِ، اللَّهُمَّ إنِّي أسألُكَ العَفوَ والعافيةَ في دِيني ودُنيايَ، وأهْلي ومالي، اللَّهُمَّ استُرْ عَوْراتي، وآمِنْ رَوْعاتي، اللَّهُمَّ احْفَظْني من بينِ يَدَيَّ، ومن خَلْفي، وعن يَميني، وعن شِمالي، ومن فَوْقي، وأعوذُ بعَظَمتِكَ أنْ أُغْتالَ من تَحْتي',
'اللهم إنا نعوذُ بك من أن نُشرِكَ بك شيئًا نعلَمُه، و نستغفرُك لما لا نعلمُه',
'يا حيُّ يا قيُّومُ، برَحمتِكَ أستَغيثُ، أصلِح لي شأني كُلَّهُ، ولا تَكِلني إلى نَفسي طرفةَ عينٍ',
'اللَّهمَّ ما أصبحَ بي من نعمةٍ أو بأحدٍ من خلقِكَ فمنكَ وحدَكَ لا شريكَ لكَ فلكَ الحمدُ ولكَ الشُّكرُ',
'اللَّهمَّ عالِمَ الغَيبِ والشَّهادةِ، فاطرَ السَّمواتِ والأرضِ، رَبَّ كلِّ شيءٍ ومَليكَهُ، أشهدُ أن لا إلَهَ إلَّا أنتَ، أعوذُ بِكَ مِن شرِّ نفسي وشرِّ الشَّيطانِ وشِركِهِ',
'(حَسبيَ اللهُ لا إلهَ إلَّا هو، عليه تَوكَّلْتُ، وهو ربُّ العَرشِ العَظيمِ)، سَبعَ مراتٍ',
'(سُبْحَانَ اللهِ وَبِحَمْدِهِ، عَدَدَ خَلْقِهِ وَرِضَا نَفْسِهِ وَزِنَةَ عَرْشِهِ وَمِدَادَ كَلِمَاتِهِ)، وهي تُقال ثلاث مرات',
'سبحانَ اللَّهِ وبحمدِهِ وهي تُقال مئةَ مرَّةٍ',
'اللَّهُمَّ إنِّي أصبَحتُ أُشهِدُك، وأُشهِدُ حَمَلةَ عَرشِكَ، ومَلائِكَتَك، وجميعَ خَلقِكَ: أنَّكَ أنتَ اللهُ لا إلهَ إلَّا أنتَ، وأنَّ مُحمَّدًا عبدُكَ ورسولُكَ',
'رَضيتُ باللَّهِ ربًّا، وبالإسلامِ دينًا، وبِمُحمَّدٍ رسولًا',
'اللَّهمَّ عافِني في بدَني اللَّهمَّ عافِني في سمعي اللَّهمَّ عافِني في بصري لا إلهَ إلَّا أنت. اللَّهمَّ إنِّي أعوذُ بِكَ منَ الكُفْرِ والفقرِ اللَّهمَّ إنِّي أعوذُ بكَ من عذابِ القبرِ لا إلهَ إلَّا أنت تعيدُها ثَلاثَ مرَّاتٍ',
'أَصْبَحْنَا وَأَصْبَحَ المُلْكُ لِلَّهِ وَالْحَمْدُ لِلَّهِ لا إلَهَ إلَّا اللَّهُ، وَحْدَهُ لا شَرِيكَ له . له المُلْكُ وَلَهُ الحَمْدُ وَهو علَى كُلِّ شيءٍ قَدِيرٌ، رَبِّ أَسْأَلُكَ خَيْرَ ما في هذِه اللَّيْلَةِ وَخَيْرَ ما بَعْدَهَا، وَأَعُوذُ بكَ مِن شَرِّ ما في هذِه اللَّيْلَةِ وَشَرِّ ما بَعْدَهَا، رَبِّ أَعُوذُ بكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ، رَبِّ أَعُوذُ بكَ مِن عَذَابٍ في النَّارِ وَعَذَابٍ في القَبْرِ',
'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ (مَن صلى عَلَيَّ حين يُصْبِحُ عَشْرًا ، وحين يُمْسِي عَشْرًا أَدْرَكَتْه شفاعتي يومَ القيامةِ)',
'أستغفرُ اللهَ العظيمَ الذي لا إلهَ إلَّا هو الحيَّ القيومَ وأتوبُ إليه',
'اللَّهمَّ إنِّي أسألُكَ عِلمًا نافعًا ورزقًا طيِّبًا وعملًا متقبَّلًا',
'أعوذُ بكلماتِ اللهِ التَّامَّاتِ مِن شرِّ ما خلَق',
'أعوذُ بكلماتِ اللهِ التَّامَّاتِ مِن شرِّ ما خلَق',
'أعوذُ بكلماتِ اللهِ التَّامَّاتِ مِن شرِّ ما خلَق',
'من قال إذا أصبَح: لا إلهَ إلَّا اللهُ وحدَه لا شريكَ له له الملكُ وله الحمدُ وهو على كلِّ شيءٍ قديرٌ عشْرَ مرَّاتٍ كُتِب له بهنَّ عشْرُ حسناتٍ ومُحي بهنَّ عنه عشْرُ سيِّئاتٍ ورُفِع له بهن عشْرُ درجاتٍ وكُنَّ له عَدْلَ عِتاقةِ أربعِ رقابٍ وكُنَّ له حرَسًا مِن الشَّيطانِ حتَّى يُمسيَ',
'آية الكرسي: (اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ الْعَظِيمُ)',
"سورة الإخلاص: (قُلْ هُوَ اللَّهُ أَحَدٌ* اللَّهُ الصَّمَدُ* لَمْ يَلِدْ وَلَمْ يُولَدْ* وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ) ثلاثا",
'سورة الفلق: (قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ* مِن شَرِّ مَا خَلَقَ* وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ* وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ* وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ) ثلاثا',
'سورة الناس: (قُلْ أَعُوذُ بِرَبِّ النَّاسِ* مَلِكِ النَّاسِ* إِلَٰهِ النَّاسِ* مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ* الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ* مِنَ الْجِنَّةِ وَالنَّاسِ) ثلاثا',
'قوله تعالى: (رَبِّ أَعُوذُ بِكَ مِنْ هَمَزَاتِ الشَّيَاطِينِ وَأَعُوذُ بِكَ رَبِّ أَنْ يَحْضُرُونِ)',
'قوله تعالى: (رَبِّ أَعُوذُ بِكَ مِنْ هَمَزَاتِ الشَّيَاطِينِ وَأَعُوذُ بِكَ رَبِّ أَنْ يَحْضُرُونِ)قوله تعالى: (حَسْبِيَ اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ ۖ عَلَيْهِ تَوَكَّلْتُ ۖ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيمِ).'
]
# =======================================================================================================================================================================================================================================================================================================================================================
AzkharAlMasaa = [
'اللَّهمَّ إنِّي عَبدُك، وابنُ عبدِك، وابنُ أمتِك، ناصِيَتي بيدِكَ، ماضٍ فيَّ حكمُكَ، عدْلٌ فيَّ قضاؤكَ، أسألُكَ بكلِّ اسمٍ هوَ لكَ سمَّيتَ بهِ نفسَك، أو أنزلْتَه في كتابِكَ، أو علَّمتَه أحدًا من خلقِك، أو استأثرتَ بهِ في علمِ الغيبِ عندَك، أن تجعلَ القُرآنَ ربيعَ قلبي، ونورَ صَدري، وجَلاءَ حَزَني، وذَهابَ هَمِّي',
'اللَّهمَّ إنِّي أسأَلُكَ مِن الخيرِ كلِّه عاجلِه وآجلِه ما علِمْتُ منه وما لَمْ أعلَمْ وأعوذُ بكَ مِن الشَّرِّ كلِّه عاجلِه وآجلِه ما علِمْتُ منه وما لَمْ أعلَمْ، اللَّهمَّ إنِّي أسأَلُكَ مِن الخيرِ ما سأَلكَ عبدُك ونَبيُّكَ وأعوذُ بكَ مِن الشَّرِّ ما عاذ به عبدُك ونَبيُّكَ وأسأَلُكَ الجنَّةَ وما قرَّب إليها مِن قولٍ وعمَلٍ وأعوذُ بكَ مِن النَّارِ وما قرَّب إليها مِن قولٍ وعمَلٍ وأسأَلُكَ أنْ تجعَلَ كلَّ قضاءٍ قضَيْتَه لي خيرًا',
'(بسمِ اللهِ الذي لا يَضرُ مع اسمِه شيءٌ في الأرضِ ولا في السماءِ وهو السميعُ العليمِ)، وتُقال ثلاث مرات',
'رَضِيتُ بِاللهِ رَبًّا، وَبِالْإِسْلَامِ دِينًا، وَبِمُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ نَبِيًّا وَرَسُولًا',
'اللَّهمَّ بِكَ أمسَينا وبِكَ أصبَحنا وبِكَ نحيا وبِكَ نموتُ وإليكَ المصير',
'اللَّهمَّ ما أمسى بي مِن نعمةٍ أو بأحَدٍ مِن خَلْقِكَ، فمنكَ وحدَكَ لا شريكَ لكَ، فلَكَ الحمدُ ولكَ الشُّكرُ، فقد أدى شُكْرَ ذلكَ اليومِ',
'سبحانَ اللَّهِ وبحمدِهِ وهي تُقال مئةَ مرَّةٍ',
'(سُبْحَانَ اللهِ وَبِحَمْدِهِ، عَدَدَ خَلْقِهِ وَرِضَا نَفْسِهِ وَزِنَةَ عَرْشِهِ وَمِدَادَ كَلِمَاتِهِ)، وهي تُقال ثلاث مرات',
'اللَّهُمَّ إنِّي أمسيت أُشهِدُك، وأُشهِدُ حَمَلةَ عَرشِكَ، ومَلائِكَتَك، وجميعَ خَلقِكَ: أنَّكَ أنتَ اللهُ لا إلهَ إلَّا أنتَ، وأنَّ مُحمَّدًا عبدُكَ ورسولُكَ',
'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ (مَن صلى عَلَيَّ حين يُصْبِحُ عَشْرًا ، وحين يُمْسِي عَشْرًا أَدْرَكَتْه شفاعتي يومَ القيامةِ)',
'لا إلهَ إلَّا اللهُ وحدَه لا شريكَ له له الملكُ وله الحمدُ وهو على كلِّ شيءٍ قديرٌ',
'أمسَيْنا على فِطرةِ الإسلامِ وعلى كَلِمةِ الإخلاصِ وعلى دينِ نبيِّنا محمَّدٍ صلَّى اللهُ عليه وسلَّم وعلى مِلَّةِ أبينا إبراهيمَ حنيفًا مسلمًا وما كان مِنَ المشركينَ',
'(اللَّهمَّ عافِني في بدَني اللَّهمَّ عافِني في سمعي اللَّهمَّ عافِني في بصري لا إلهَ إلَّا أنت، اللَّهمَّ إنِّي أعوذُ بِكَ منَ الكُفْرِ والفقرِ اللَّهمَّ إنِّي أعوذُ بكَ من عذابِ القبرِ لا إلهَ إلَّا أنت) وتقال ثَلاثَ مرَّاتٍ',
'اللهم إنا نعوذُ بك من أن نُشرِكَ بك شيئًا نعلَمُه، و نستغفرُك لما لا نعلمُه',
'أستغفرُ اللهَ العظيمَ الذي لا إلهَ إلَّا هو الحيَّ القيومَ وأتوبُ إليه',
'اللَّهمَّ إنِّي أسألُكَ عِلمًا نافعًا ورزقًا طيِّبًا وعملًا متقبَّلًا',
'اللَّهمَّ إنِّي أسألُكَ عِلمًا نافعًا ورزقًا طيِّبًا وعملًا متقبَّلًايا حيُّ يا قيُّومُ، برَحمتِكَ أستَغيثُ، أصلِح لي شأني كُلَّهُ، ولا تَكِلني إلى نَفسي طرفةَ عينٍ',
'اللَّهمَّ عالِمَ الغَيبِ والشَّهادةِ، فاطرَ السَّمواتِ والأرضِ، رَبَّ كلِّ شيءٍ ومَليكَهُ، أشهدُ أن لا إلَهَ إلَّا أنتَ، أعوذُ بِكَ مِن شرِّ نفسي وشرِّ الشَّيطانِ وشِركِهِ',
'اللهمَّ فاطرَ السمواتِ والأرضِ، عالمَ الغيبِ والشهادةِ، لا إلهَ إلَّا أنتَ ربَّ كلِّ شيءٍ ومَليكَه، أعوذُ بك من شرِّ نفسي ومن شرِّ الشيطانِ وشرَكِه، وأنْ أقترفَ على نفسي سوءًا أو أجرَّهُ إلى مسلمٍ',
'اللهمَّ إنِّي أعوذُ بك من الهمِّ والحزنِ، والعجزِ والكسلِ، والبُخلِ والجُبنِ، وضَلَعِ الدَّينِ، وغَلَبَةِ الرجالِ',
'أعوذُ بكلماتِ اللهِ التَّامَّاتِ مِن شرِّ ما خلَق',
'اللهمَّ إني أسألُك العفوَ والعافيةَ، في الدنيا والآخرةِ، اللهمَّ إني أسألُك العفوَ والعافيةَ، في دِيني ودنيايَ وأهلي ومالي، اللهمَّ استُرْ عوراتي، وآمِنْ روعاتي، واحفظني من بين يدي، ومن خلفي، وعن يميني، وعن شمالي، ومن فوقي، وأعوذُ بك أن أُغْتَالَ من تحتي',
'أَمْسَيْنَا وَأَمْسَى المُلْكُ لِلَّهِ، وَالْحَمْدُ لِلَّهِ لا إلَهَ إلَّا اللَّهُ، وَحْدَهُ لا شَرِيكَ له، له المُلْكُ وَلَهُ الحَمْدُ وَهو علَى كُلِّ شيءٍ قَدِيرٌ، رَبِّ أَسْأَلُكَ خَيْرَ ما في هذِه اللَّيْلَةِ وَخَيْرَ ما بَعْدَهَا، وَأَعُوذُ بكَ مِن شَرِّ ما في هذِه اللَّيْلَةِ وَشَرِّ ما بَعْدَهَا، رَبِّ أَعُوذُ بكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ، رَبِّ أَعُوذُ بكَ مِن عَذَابٍ في النَّارِ وَعَذَابٍ في القَبْرِ',
'اللَّهُمَّ أنْتَ رَبِّي لا إلَهَ إلَّا أنْتَ، خَلَقْتَنِي وأنا عَبْدُكَ، وأنا علَى عَهْدِكَ ووَعْدِكَ ما اسْتَطَعْتُ، أعُوذُ بكَ مِن شَرِّ ما صَنَعْتُ، أبُوءُ لكَ بنِعْمَتِكَ عَلَيَّ، وأَبُوءُ لكَ بذَنْبِي فاغْفِرْ لِي، فإنَّه لا يَغْفِرُ الذُّنُوبَ إلَّا أنْتَ',
'اللَّهمَّ إنِّي أسألُكَ خيرَ هذه الليلة فتحَها، ونصرَها، ونورَها، وبرَكتَها، وَهداها، وأعوذُ بِكَ من شرِّ ما فيها وشرِّ ما بعدَها',
'آية الكرسي: (اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ الْعَظِيمُ)',
"قال تعالى في سورة البقرة أيضاً: (آمَنَ الرَّسُولُ بِمَا أُنزِلَ إِلَيْهِ مِن رَّبِّهِ وَالْمُؤْمِنُونَ ۚ كُلٌّ آمَنَ بِاللَّهِ وَمَلَائِكَتِهِ وَكُتُبِهِ وَرُسُلِهِ لَا نُفَرِّقُ بَيْنَ أَحَدٍ مِّن رُّسُلِهِ ۚ وَقَالُوا سَمِعْنَا وَأَطَعْنَا ۖ غُفْرَانَكَ رَبَّنَا وَإِلَيْكَ الْمَصِيرُ*لَا يُكَلِّفُ اللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا اكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَا إِن نَّسِينَا أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَا إِصْرًا كَمَا حَمَلْتَهُ عَلَى الَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِ ۖ وَاعْفُ عَنَّا وَاغْفِرْ لَنَا وَارْحَمْنَا ۚ أَنتَ مَوْلَانَا فَانصُرْنَا عَلَى الْقَوْمِ الْكَافِرِينَ)",
"سورة الإخلاص: (قُلْ هُوَ اللَّهُ أَحَدٌ* اللَّهُ الصَّمَدُ* لَمْ يَلِدْ وَلَمْ يُولَدْ* وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ) ثلاثا",
'سورة الفلق: (قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ* مِن شَرِّ مَا خَلَقَ* وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ* وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ* وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ) ثلاثا',
'سورة الناس: (قُلْ أَعُوذُ بِرَبِّ النَّاسِ* مَلِكِ النَّاسِ* إِلَٰهِ النَّاسِ* مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ* الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ* مِنَ الْجِنَّةِ وَالنَّاسِ) ثلاثا'
]

def story(PageName, Text):
	pyautogui.moveTo(950, 300, duration=1)
	time.sleep(2)
	pyautogui.click()
	pyautogui.moveTo(900, 200, duration=1)
	time.sleep(2)
	pyautogui.click()
	pyautogui.write(PageName)
	time.sleep(2)
	pyautogui.moveTo(970, 270, duration=1)
	time.sleep(6)
	pyautogui.click()
	pyautogui.moveTo(1000, 500, duration=1)
	time.sleep(2)
	pyautogui.click()
	pyautogui.moveTo(150, 400, duration=1)
	time.sleep(2)
	pyautogui.click()
	# Store our string to the clipboard
	pyperclip.copy(Text)
	# Hotkey the paste command
	pyautogui.hotkey("ctrl", "v")
	pyautogui.moveTo(250, 700, duration=1)
	time.sleep(2)
	pyautogui.click()

x = int(input('Enter the type (0 for test, 1 for AzkharAlsabah, 2 for AzkharAlMasaa): '))
if x == 0:
	webbrowser.open_new('https://business.facebook.com/creatorstudio/home')
	time.sleep(10)
	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlsabah Done on {datetime.datetime.now().time()}✔')
elif x == 1:
	webbrowser.open_new('https://business.facebook.com/creatorstudio/home')
	time.sleep(10)
	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlsabah Starts')
	for i in AzkharAlsabah:
		story('apocryphon', i)
		time.sleep(2)
	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlsabah Done on {datetime.datetime.now().time()}✔')
elif x == 2:
	webbrowser.open_new('https://business.facebook.com/creatorstudio/home')
	time.sleep(10)
	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlMasaa Starts')
	for i in AzkharAlMasaa:
		story('apocryphon', i)
		time.sleep(2)
	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlMasaa Done on {datetime.datetime.now().time()}✔')