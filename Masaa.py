# coding=utf8
import time
import logging
import datetime
import webbrowser

import pyautogui
import pyperclip

logging.basicConfig(filename='azkhar.log', level=logging.INFO,
	format='%(asctime)s  - %(levelno)s | %(message)s')

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
	pyautogui.moveTo(1260, 200, duration=1)
	time.sleep(3)
	pyautogui.click()
	pyautogui.moveTo(900, 200, duration=1)
	time.sleep(3)
	pyautogui.click()
	pyautogui.write(PageName)
	time.sleep(3)
	pyautogui.moveTo(970, 270, duration=1)
	time.sleep(6)
	pyautogui.click()
	pyautogui.moveTo(1000, 500, duration=1)
	time.sleep(3)
	pyautogui.click()
	pyautogui.moveTo(150, 400, duration=1)
	time.sleep(3)
	pyautogui.click()
	# Store our string to the clipboard
	pyperclip.copy(Text)
	# Hotkey the paste command
	pyautogui.hotkey("ctrl", "v")
	pyautogui.moveTo(250, 700, duration=1)
	time.sleep(3)
	pyautogui.click()

if __name__ == '__main__':
	start_time = datetime.datetime.now()
	print(f'{start_time} | Starting')
	webbrowser.open_new('https://business.facebook.com/creatorstudio/published_stories?content_table=POSTED_POSTS')
	time.sleep(15)
	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlMasaa Starts')
	for nm in range(11):
		time.sleep(nm)
		if pyautogui.pixelMatchesColor(253, 703 , (0, 164, 0)):
			print("GO!")
			break
		if nm == 10:
			logging.debug('GO gone wrong!')

	for i in AzkharAlMasaa:
		starting_time = datetime.datetime.now()
		logging.info(f'{starting_time} | Start {AzkharAlMasaa.index(i)}')
		story('apocryphon', i)
		for nm in range(11):
			time.sleep(nm)
			if pyautogui.pixelMatchesColor(253, 703, (0, 164, 0)):
				print(f'{(AzkharAlMasaa.index(i)+1)}/{len(AzkharAlMasaa)} : {round((AzkharAlMasaa.index(i)+1)/len(AzkharAlMasaa) * 100, 1)}%')
				break
			if nm == 10:
				logging.debug(f'{AzkharAlMasaa.index(i)}/{len(AzkharAlMasaa)} on AzkharAlMasaa!?')

		ending_time = datetime.datetime.now()
		logging.info(f'{ending_time} | Done {AzkharAlMasaa.index(i)}')
		logging.info('Duration: {}'.format(ending_time - starting_time))
		logging.info('\n')

	story('apocryphon', f'{datetime.datetime.now().date()} AzkharAlMasaa Done on {datetime.datetime.now().time()}✔')
	for nm in range(11):
		time.sleep(nm)
		if pyautogui.pixelMatchesColor(253, 703, (0, 164, 0)):
			print("FINISH!")
			break
		if nm == 10:
			logging.debug("FINISH gone wrong!?")
	end_time = datetime.datetime.now()
	logging.info(f'{end_time} | Quit')
	print(f'{end_time} | Quit')
	logging.info('Duration: {}'.format(end_time - start_time))