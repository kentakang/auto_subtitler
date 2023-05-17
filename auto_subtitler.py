import stable_whisper
import os
from srtranslator import SrtFile
from srtranslator.translators.deepl_scrap import DeeplTranslator
from webdriverdownloader import GeckoDriverDownloader

geckoDownloader = GeckoDriverDownloader()

geckoDownloader.download_and_install(os_name='macos', bitness='-aarch64')

translator = DeeplTranslator()
whisper_model = stable_whisper.load_model('base')
target_path = './'
target_ext = '.mp4'
target_files = [f for f in os.listdir(target_path) if f.endswith(target_ext)]

for target_file in target_files:
  print('Processing {}'.format(target_file))

  video_name = target_file.replace(target_ext, '')
  result = whisper_model.transcribe(target_path + target_file)
  srt_file_name = video_name + '.srt'
  srt_file_path = target_path + srt_file_name

  result.to_srt_vtt(srt_file_path)

  srt = SrtFile(srt_file_path)
  
  srt.translate(translator, 'ja', 'ko')
  srt.wrap_lines()
  srt.save(srt_file_path)
  print('Complete processing for {}'.format(target_file))

translator.quit()