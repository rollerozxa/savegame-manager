meta:
  id: savegame_banner
  file-extension: bin
  endian: be
seq:
  - id: magic
    contents: ["W","I","B","N"]
  - id: flags
    type: u4
  - id: anim_speed
    type: u2
  - id: reserved
    size: 22
  - id: game_title
    type: str
    size: 64
    encoding: UTF-16BE
  - id: game_subtitle
    type: str
    size: 64
    encoding: UTF-16BE
  - id: banner
    size: 24576
  - id: icon_frames
    size: 4608
    repeat: eos
