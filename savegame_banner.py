# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
	raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SavegameBanner(KaitaiStruct):
	def __init__(self, _io, _parent=None, _root=None):
		self._io = _io
		self._parent = _parent
		self._root = _root if _root else self
		self._read()

	def _read(self):
		self.magic = self._io.read_bytes(4)
		if not self.magic == b"\x57\x49\x42\x4E":
			raise kaitaistruct.ValidationNotEqualError(b"\x57\x49\x42\x4E", self.magic, self._io, u"/seq/0")
		self.flags = self._io.read_u4be()
		self.anim_speed = self._io.read_u2be()
		self.reserved = self._io.read_bytes(22)
		self.game_title = (self._io.read_bytes(64)).decode(u"UTF-16BE")
		self.game_subtitle = (self._io.read_bytes(64)).decode(u"UTF-16BE")
		self.banner = self._io.read_bytes(24576)
		self.icon_frames = []
		i = 0
		while not self._io.is_eof():
			self.icon_frames.append(self._io.read_bytes(4608))
			i += 1
