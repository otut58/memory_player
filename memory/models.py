from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

WEAPON = ( 
    ('ボールドマーカー', 'ボールドマーカー'), ('わかばシューター', 'わかばシューター'), ('もみじシューター', 'もみじシューター'), ('シャープマーカー', 'シャープマーカー'), ('プロモデラーMG', 'プロモデラーMG'),
    ('プロモデラーRG', 'プロモデラーRG'), ('スプラシューター', 'スプラシューター'), ('スプラシューターコラボ', 'スプラシューターコラボ'), ('.52ガロン', '.52ガロン'), ('N-ZAP85', 'N-ZAP85'), 
    ('プライムシューター', 'プライムシューター'), ('プライムシューターコラボ', 'プライムシューターコラボ'), ('.96ガロン', '.96ガロン'), ('ジェットスイーパー', 'ジェットスイーパー'), ('スペースシューター', 'スペースシューター'),
    ('L3リールガン', 'L3リールガン'), ('H3リールガン', 'H3リールガン'),  
    ('ボトルガイザー', 'ボトルガイザー'),
    ('ノヴァブラスター', 'ノヴァブラスター'), ('ノヴァブラスターネオ', 'ノヴァブラスターネオ'), ('ホットブラスター', 'ホットブラスター'), ('ロングブラスター', 'ロングブラスター'), ('クラッシュブラスター', 'クラッシュブラスター'),
    ('ラピッドブラスター', 'ラピッドブラスター'), ('Rブラスターエリート', 'Rブラスターエリート'),
    ('カーボンローラー', 'カーボンローラー'), ('カーボンローラーデコ', 'カーボンローラーデコ'), ('スプラローラー', 'スプラローラー'), ('ダイナモローラー', 'ダイナモローラー'), ('ヴァリアブルローラー', 'ヴァリアブルローラー'), 
    ('ワイドローラー', 'ワイドローラー'),('パブロ', 'パブロ'), ('パブロ・ヒュー', 'パブロ・ヒュー'), ('ホクサイ', 'ホクサイ'),
    ('スクイックリン', 'スクイックリン'), ('スプラチャージャー', 'スプラチャージャー'), ('スプラスコープ', 'スプラスコープ'), ('リッター4K', 'リッター4K'), ('4Kスコープ', '4Kスコープ'), 
    ('14式竹筒銃・甲', '14式竹筒銃・甲'), ('ソイチューバー', 'ソイチューバー'), ('R-PEN/5H', 'R-PEN/5H'),
    ('バケットスロッシャー', 'バケットスロッシャー'), ('バケットスロッシャーデコ', 'バケットスロッシャーデコ'), ('ヒッセン', 'ヒッセン'), ('スクリュースロッシャー', 'スクリュースロッシャー'), ('オーバーフロッシャー', 'オーバフロッシャー'), ('エクスプロッシャー', 'エクスプロッシャー'),
    ('スプラスピナー', 'スプラスピナー'), ('スプラスピナーコラボ', 'スプラスピナーコラボ'), ('バレルスピナー', 'バレルスピナー'), ('ハイドラント', 'ハイドラント'), ('クーゲルシュライーバー', 'クーゲルシュライーバー'), 
    ('ノーチラス47', 'ノーチラス47'),
    ('スパッタリー', 'スパッタリー'), ('スパッタリー・ヒュー', 'スパッタリー・ヒュー'), ('スプラマニューバー', 'スプラマニューバー'), ('ケルビン525', 'ケルビン525'), ('デュアルスイーパー', 'デュアルスイーパー'), ('クアッドホッパーブラック', 'クアッドホッパーブラック'),
    ('パラシェルター', 'パラシェルター'), ('キャンピングシェルター', 'キャンピングシェルター'), ('スパイガジェット', 'スパイガジェット'),
    ('ジムワイパー', 'ジムワイパー'), ('ドライブワイパー', 'ドライブワイパー'),
)

STAGE = ( ('ユノハナ大渓谷', 'ユノハナ大渓谷'), ('ゴンズイ地区', 'ゴンズイ地区'), ('ヤガラ市場', 'ヤガラ市場'), ('マテガイ放水路', 'マテガイ放水路'), ('ナメロウ金属', 'ナメロウ金属'),
('マヒマヒリゾート&スパ', 'マヒマヒリゾート&スパ'), ('キンメダイ美術館', 'キンメダイ美術館'), ('マサバ海峡大橋', 'マサバ海峡大橋'), ('海女美術大学', '海女美術大学'), ('チョウザメ造船', 'チョウザメ造船'), 
('ザトウマーケット', 'ザトウマーケット'), ('スメーシーワールド', 'スメーシーワールド'), ('ヒラメが丘団地', 'ヒラメが丘団地'), ('クサヤ温泉', 'クサヤ温泉')
)

RULE = (('ナワバリバトル', 'ナワバリバトル'), ('ガチエリア', 'ガチエリア'), ('ガチヤグラ', 'ガチヤグラ'), ('ガチホコバトル', 'ガチホコバトル'), ('ガチアサリ', 'ガチアサリ'))

class Memory(models.Model):
    title = models.CharField('タイトル', max_length=128)
    weapon = models.CharField('ブキ', max_length=128, choices=WEAPON)
    stage = models.CharField('ステージ', max_length=128, choices=STAGE)
    rule = models.CharField('ルール', max_length=128, choices=RULE)
    xp = models.IntegerField('xp', validators=[MinValueValidator(900), MaxValueValidator(4000)])
    memory_num = models.SlugField('バトルメモリーのコード', max_length=19)
    comment = models.TextField('投稿者コメント', blank=True)

    def __str__(self):
        return self.title

class Viewer_Comment(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    viewer_comment = models.TextField('視聴者コメント')
