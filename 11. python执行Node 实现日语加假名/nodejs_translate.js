const KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji");
const Kuroshiro = require("kuroshiro")
const kuroshiro = new Kuroshiro.default();
kuroshiro.init(new KuromojiAnalyzer())
.then(function () {
    return kuroshiro.convert(ja_content, {mode:"furigana", to:"hiragana"});
})
.then(function(result){
  console.log(result);
  //shingeki no kyojin
})
