function hash(_0x26fbb9) {
  function _0x3c7cb0(_0x4e55d9, _0x25dd3b) {
    return (_0x4e55d9 & 2147483647) + (_0x25dd3b & 2147483647) ^ _0x4e55d9 & 2147483648 ^ _0x25dd3b & 2147483648;
  }

  function _0x10484f(_0x1c3232) {
    var _0x34d2ea = "0123456789abcdef";
    var _0x11469e = "";

    for (var _0x50191d = 7; _0x50191d >= 0; _0x50191d--) {
      _0x11469e += _0x34d2ea["charAt"](_0x1c3232 >> _0x50191d * 4 & 15);
    }

    return _0x11469e;
  }

  function _0x376c53(_0x195517) {
    var _0x3feff5 = (_0x195517["length"] + 8 >> 6) + 1,
        _0x579bb9 = new Array(_0x3feff5 * 16);

    for (var _0x3a8d21 = 0; _0x3a8d21 < _0x3feff5 * 16; _0x3a8d21++) {
      _0x579bb9[_0x3a8d21] = 0;
    }

    for (_0x3a8d21 = 0; _0x3a8d21 < _0x195517["length"]; _0x3a8d21++) {
      _0x579bb9[_0x3a8d21 >> 2] |= _0x195517["charCodeAt"](_0x3a8d21) << 24 - (_0x3a8d21 & 3) * 8;
    }

    _0x579bb9[_0x3a8d21 >> 2] |= 128 << 24 - (_0x3a8d21 & 3) * 8;
    _0x579bb9[_0x3feff5 * 16 - 1] = _0x195517["length"] * 8;
    return _0x579bb9;
  }

  function _0x469e6e(_0x4d8aea, _0x1056c3) {
    return _0x4d8aea << _0x1056c3 | _0x4d8aea >>> 32 - _0x1056c3;
  }

  function _0x245ece(_0x39f65f, _0x200bce, _0x2be6c9, _0x19819e) {
    if (_0x39f65f < 20) {
      return _0x200bce & _0x2be6c9 | ~_0x200bce & _0x19819e;
    }

    if (_0x39f65f < 40) {
      return _0x200bce ^ _0x2be6c9 ^ _0x19819e;
    }

    if (_0x39f65f < 60) {
      return _0x200bce & _0x2be6c9 | _0x200bce & _0x19819e | _0x2be6c9 & _0x19819e;
    }

    return _0x200bce ^ _0x2be6c9 ^ _0x19819e;
  }

  function _0x435520(_0x2d8bc4) {
    return _0x2d8bc4 < 20 ? 1518500249 : _0x2d8bc4 < 40 ? 1859775393 : _0x2d8bc4 < 60 ? -1894007588 : -899497514;
  }

  var _0x5eede0 = _0x376c53(_0x26fbb9);

  var _0x250629 = new Array(80);

  var _0x3c11de = 1732584193;

  var _0x5c9f00 = -271733879;

  var _0x4450c4 = -1732584194;

  var _0x7186c1 = 271733878;

  var _0x29b70e = -1009589776;

  for (var _0x4d2fc4 = 0; _0x4d2fc4 < _0x5eede0["length"]; _0x4d2fc4 += 16) {
    var _0x2d4533 = _0x3c11de;
    var _0x42c8f9 = _0x5c9f00;
    var _0x432cba = _0x4450c4;
    var _0x26c07c = _0x7186c1;
    var _0x3aad61 = _0x29b70e;

    for (var _0x188bd6 = 0; _0x188bd6 < 80; _0x188bd6++) {
      if (_0x188bd6 < 16) {
        _0x250629[_0x188bd6] = _0x5eede0[_0x4d2fc4 + _0x188bd6];
      } else {
        _0x250629[_0x188bd6] = _0x469e6e(_0x250629[_0x188bd6 - 3] ^ _0x250629[_0x188bd6 - 8] ^ _0x250629[_0x188bd6 - 14] ^ _0x250629[_0x188bd6 - 16], 1);
      }

      t = _0x3c7cb0(_0x3c7cb0(_0x469e6e(_0x3c11de, 5), _0x245ece(_0x188bd6, _0x5c9f00, _0x4450c4, _0x7186c1)), _0x3c7cb0(_0x3c7cb0(_0x29b70e, _0x250629[_0x188bd6]), _0x435520(_0x188bd6)));
      _0x29b70e = _0x7186c1;
      _0x7186c1 = _0x4450c4;
      _0x4450c4 = _0x469e6e(_0x5c9f00, 30);
      _0x5c9f00 = _0x3c11de;
      _0x3c11de = t;
    }

    _0x3c11de = _0x3c7cb0(_0x3c11de, _0x2d4533);
    _0x5c9f00 = _0x3c7cb0(_0x5c9f00, _0x42c8f9);
    _0x4450c4 = _0x3c7cb0(_0x4450c4, _0x432cba);
    _0x7186c1 = _0x3c7cb0(_0x7186c1, _0x26c07c);
    _0x29b70e = _0x3c7cb0(_0x29b70e, _0x3aad61);
  }

  return _0x10484f(_0x3c11de) + _0x10484f(_0x5c9f00) + _0x10484f(_0x4450c4) + _0x10484f(_0x7186c1) + _0x10484f(_0x29b70e);
}

function go(_0x1830f5) {

  var _0x5e8f37 = new Date();

  function _0x475e1a(_0x41f9f0, _0x1ea4ab) {
    var _0x1deb19 = _0x1830f5["chars"]["length"];

    for (var _0x369878 = 0; _0x369878 < _0x1deb19; _0x369878++) {
      for (var _0x4b3803 = 0; _0x4b3803 < _0x1deb19; _0x4b3803++) {
        var _0x3ea464 = _0x1ea4ab[0] + _0x1830f5["chars"]["substr"](_0x369878, 1) + _0x1830f5["chars"]["substr"](_0x4b3803, 1) + _0x1ea4ab[1];

        if (hash(_0x3ea464) == _0x41f9f0) {
          return [_0x3ea464, new Date() - _0x5e8f37];
        }
      }
    }
  };

  var _0x3ca3c1 = _0x475e1a(_0x1830f5["ct"], _0x1830f5["bts"]);

  if (_0x3ca3c1) {
    var _0x5c5787;

    if (_0x1830f5["wt"]) {
      _0x5c5787 = parseInt(_0x1830f5["wt"]) > _0x3ca3c1[1] ? parseInt(_0x1830f5["wt"]) - _0x3ca3c1[1] : 500;
    } else {
      _0x5c5787 = 1500;
    }
    var document = {}
    function get_cookie() {
      document["cookie"] = _0x1830f5["tn"] + "=" + _0x3ca3c1[0] + ";Max-age=" + _0x1830f5["vt"] + "; path = /";
      // console.log(document)
      return document
    };
    document = get_cookie()
    return document
  } 
}


document = go({
  "bts": ["1612591315.626|0|tvW", "LKDYryx85Bwp9rVOPZSENc%3D"],
  "chars": "xLDiTrvqXWwbJrnoMkdZbB",
  "ct": "5d124aec3207ea03dd5c1abe60ce4338281c8725",
  "ha": "sha1",
  "tn": "__jsl_clearance",
  "vt": "3600",
  "wt": "1500"
});

// document = go({
// 	"bts": ["1615366819.759|0|gxS", "bqmFfJfnXV2%2F6KvCL%2Br3L4%3D"],
// 	"chars": "NJoDzTEdqVMBVkspySpGVG",
// 	"ct": "04962824ae6c3a6be2d457d4776a39ad378c0b3f86c72fb9a6640707e93fc23e",
// 	"ha": "sha256",
// 	"tn": "__jsl_clearance",
// 	"vt": "3600",
// 	"wt": "1500"
// });
// console.log(document)
console.log(document["cookie"].replace("Max-age=3600; path = /",""))
