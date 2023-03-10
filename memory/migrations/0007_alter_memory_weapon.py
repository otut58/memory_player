# Generated by Django 4.1.7 on 2023-02-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0006_alter_memory_weapon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='weapon',
            field=models.CharField(choices=[('Sploosh-o-matic', 'ボールドマーカー'), ('Splattershot Jr.', 'わかばシューター'), ('Custom Splattershot Jr.', 'もみじシューター'), ('Splash-o-matic', 'シャープマーカー'), ('Aerospray MG', 'プロモデラーMG'), ('Aeropray RG', 'プロモデラーRG'), ('Splattershot', 'スプラシューター'), ('Tentatek SplatterShot', 'スプラシューターコラボ'), ('.52 Gal', '.52ガロン'), ("N-ZAP'85", 'N-ZAP85'), ('Splattershot Pro', 'プライムシューター'), ('Tentatek Splattershot', 'プライムシューターコラボ'), ('.96 Gal', '.96ガロン'), ('Jet Squelcher', 'ジェットスイーパー'), ('Splattershot Nova', 'スペースシューター'), ('L-3 Nozzlenose', 'L3リールガン'), ('H-3 Nozzlenose', 'H-3リールガン'), ('Squeezer', 'ボトルガイザー'), ('Luna Blaster', 'ノヴァブラスター'), ('Luna Blaster Neo', 'ノヴァブラスターネオ'), ('Blaster', 'ホットブラスター'), ('Range Blaster', 'ロングブラスター'), ('Clash Blaster', 'クラッシュブラスター'), ('Rapid Blaster', 'ラピッドブラスター'), ('Rapid Blaster Pro', 'ラピッドブラスターエリート'), ('Carbon Roller', 'カーボンローラー'), ('Carbon Roller Deco', 'カーボンローラーデコ'), ('Splat Roller', 'スプラローラー'), ('Dynamo Roller', 'ダイナモローラー'), ('Flingza Roller', 'ヴァリアブルローラー'), ('Big Swig Roller', 'ワイドローラー'), ('Inkbrush', 'パブロ'), ('Inkbrush Nouveau', 'パブロ・ヒュー'), ('Octobrush', 'ホクサイ'), ('Clasic Squiffer', 'スクイックリン'), ('Splat Charfer', 'スプラチャージャー'), ('Firefin Splatterscope', 'スプラスコープ'), ('E-liter 4K', 'リッター4K'), ('E-liter 4K Scope', '4Kスコープ'), ('Bamboozler 14 Mk I', '14式竹筒銃・甲'), ('Goo Tuber', 'ソイチューバー'), ('Snipewriter 5H', 'R-PEN/5H'), ('Slosher', 'バケットスロッシャー'), ('Slosher Deco', 'バケットスロッシャーデコ'), ('Tri-Slosher', 'ヒッセン'), ('Sloshing Machine', 'スクリュースロッシャー'), ('Bloblobber', 'オーバフロッシャー'), ('Explosher', 'エクスプロッシャー'), ('Mini Splatling', 'スプラスピナー'), ('Zink Mini Splatling', 'スプラスピナーコラボ'), ('Heavy Splatling', 'バレルスピナー'), ('Hydra Splatling', 'ハイドラント'), ('Ballpoint Splatling', 'クーゲルシュラーバー'), ('Nautilus 47', 'ノーチラス47')], max_length=128),
        ),
    ]
