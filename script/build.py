#! /usr/bin/env python3

import common, os, subprocess, sys

def main():
  os.chdir(os.path.join(os.path.dirname(__file__), os.pardir, 'skia'))

  build_type = common.build_type()
  classifier = common.classifier()
  machine    = common.machine()
  system     = common.system()
  ndk        = common.ndk()
  args = [
    'target_cpu="' + machine + '"',
    'skia_enable_pdf = false',
    'skia_enable_skottie = false',
    'skia_enable_tools = true',
    'skia_use_angle = false',
    'skia_use_gl = true',
    'skia_use_icu = false',
    'skia_use_lua = false',
    'skia_use_piex = false',
    'skia_use_zlib = false'
  ]
  if build_type == 'Debug':
    args += ['is_debug = true']

  if classifier == '-clang':
    if system == 'windows':
      args += ['clang_win = ' + os.path.abspath("C:/Program Files/LLVM")]
    else:
      args += [
        'cc = "clang"',
        'cxx = "clang++"'
      ]
  if system == 'android':
    args += [
      'skia_use_system_freetype2=false',
      'ndk="'+ ndk + '"'
    ]
  elif system == 'linux':
    args += [
      'extra_cflags_cc = ["-frtti"]'
    ]
  elif system == 'macos':
    args += [
      'extra_cflags_cc = ["-frtti"]'
    ]
  elif system == 'windows':
    args += ['skia_use_wuffs = false']
    if build_type == 'Debug':
      args += ['skia_enable_spirv_validation = false']
      if classifier == '-clang':
        args += ['extra_cflags_cc = [\"-fms-compatibility -MTd -D_DEBUG -DDEBUG\"]']
    elif build_type == 'Release' and classifier == '-clang':
      args += ['extra_cflags_cc = [\"-fms-compatibility\"]']
  """
  args += [
    'target_cpu="' + machine + '"',
    'skia_use_system_expat = false',
    'skia_use_system_libjpeg_turbo = false',
    'skia_use_system_libpng = false',
    'skia_use_system_libwebp = false',
    'skia_use_system_zlib = false',
    'skia_use_sfntly = false',
    'skia_use_freetype = true',
    # 'skia_use_harfbuzz = true',
    'skia_use_system_harfbuzz = false',
    'skia_pdf_subset_harfbuzz = true',
    # 'skia_use_icu = true',
    'skia_use_system_icu = false',
    # 'skia_enable_skshaper = true',
    # 'skia_enable_svg = true',
    'skia_enable_skottie = true'
  ]
  if 'macos' == system:
    args += [
      'skia_use_system_freetype2 = false',
      # 'skia_enable_gpu = true',
      # 'skia_use_gl = true',
      'skia_use_metal = true',
      'extra_cflags_cc = ["-frtti"]'
    ]
    if 'arm64' == machine:
      args += ['extra_cflags = ["-stdlib=libc++"]']
    else:
      args += ['extra_cflags = ["-stdlib=libc++", "-mmacosx-version-min=10.13"]']
  elif 'linux' == system:
    args += [
      'skia_use_system_freetype2 = true',
      # 'skia_enable_gpu = true',
      # 'skia_use_gl = true',
      'extra_cflags_cc = ["-frtti"]'
    ]
  elif 'windows' == system:
    args += [
      'skia_use_system_freetype2 = false',
      # 'skia_use_angle = true',
      'skia_use_direct3d = true',
      'extra_cflags = ["-DSK_FONT_HOST_USE_SYSTEM_SETTINGS"]',
    ]
  elif 'android' == system:
    args += [
      'skia_use_system_freetype2 = false',
      'ndk = "'+ ndk + '"'
    ]
  """
  out = os.path.join('out', system + classifier + '-' + machine + '-' + build_type + '-static').lower()
  subprocess.check_call([os.path.join('bin', 'gn'), 'gen', out, '--args=' + ' '.join(args)])

# subprocess.check_call([os.path.join('..', 'depot_tools', 'ninja'), '-C', out, 'skia'])
  subprocess.check_call(['ninja', '-C', out, 'skia'])

  return 0

if __name__ == '__main__':
  sys.exit(main())
