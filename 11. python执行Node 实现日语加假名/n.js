const KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji");
const Kuroshiro = require("kuroshiro")
const kuroshiro = new Kuroshiro.default();
kuroshiro.init(new KuromojiAnalyzer())

function translate(content){
    .then(function () {
    return kuroshiro.convert(content, {mode:"furigana", to:"hiragana"});
})
.then(function(result){
  return result
  //shingeki no kyojin
})
}