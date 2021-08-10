function _yrxULK(_yrx7jl) {
  var _yrxrqQ = [0, 1, 3, 7, 0xf, 0x1f];
  return (_yrx7jl >> _yrxS27._yrxS27) | ((_yrx7jl & _yrxrqQ[_yrxS27._yrxS27]) << (6 - _yrxS27._yrxS27))
}


function _yrxTXe(_yrx_cw) {
  var _yrxrqQ = _yrx_cw % 64;
  var _yrx$Kn = _yrx_cw - _yrxrqQ;
  _yrxrqQ = _yrxULK(_yrxrqQ);
  _yrxrqQ ^= _yrxS27._yrxDkc;
  _yrx$Kn += _yrxrqQ;
  return _yrxI6a[_yrx$Kn]
}
_yrxWFt = _yrxTXe;
var _yrxCJw = parseInt(_yrxWFt(18));

function _yrxyA$(_yrx7jl, _yrxcze) {
  try {
      if (typeof _yrx7jl !== "string")
          _yrx7jl += ''
  } catch (_yrxrqQ) {
      return _yrx7jl
  }
  if (!(_yrxCJw & 1024)) {
      _yrx7jl = _yrxR2F(_yrx7jl)
  }
  var _yrx$Kn = _yrxtSa(_yrx7jl);
  if (_yrx$Kn === null) {
      return _yrx7jl
  }
  if (_yrx$Kn._yrxKni > 3) {
      return _yrxtY2(_yrx$Kn)
  }
  var _yrxmEu = _yrxWKg(_yrxyHJ(_yrx5XG(_yrx$Kn._yrx2ad + _yrx$Kn._yrxAmM)));
  var _yrx7jl = _yrx$Kn._yrxCiX + _yrx$Kn._yrxAmM;
  if (_yrx$Kn._yrxAmM === '')
      _yrx7jl = _yrx7jl + '?';
  else
      _yrx7jl = _yrx7jl + '&';
  var _yrx2LR = _yrx$Kn._yrxiv8 + _yrx7jl;
  _yrx2LR += _yrxBXT(779, _yrx$Kn._yrxQZs, _yrxmEu, _yrxcze);
  _yrx2LR += _yrx$Kn._yrxcFt;
  console.log("_yrx2LR",_yrx2LR)
  return _yrx2LR
}
var a = "/api/loginInfo?"
var b
console.log(_yrxyA$(a,b))