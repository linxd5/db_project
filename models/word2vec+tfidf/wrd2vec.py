#!/usr/bin/env python
# coding=utf-8

from jieba_seg import jieba_seg
import gensim


doc= """素胚勾勒出青花笔锋浓转淡
瓶身描绘的牡丹一如你初妆
冉冉檀香透过窗心事我了然
宣纸上走笔至此搁一半
釉色渲染仕女图韵味被私藏
而你嫣然的一笑如含苞待放
你的美一缕飘散
去到我去不了的地方

天青色等烟雨
而我在等你
炊烟袅袅升起
隔江千万里
在瓶底书汉隶仿前朝的飘逸
就当我为遇见你伏笔
天青色等烟雨
而我在等你
月色被打捞起
晕开了结局
如传世的青花瓷自顾自美丽
你眼带笑意
色白花青的锦鲤跃然於碗底
临摹宋体落款时却惦记着你
你隐藏在窑烧里千年的秘密
极细腻犹如绣花针落地
帘外芭蕉惹骤雨
门环惹铜绿
而我路过那江南小镇惹了你
在泼墨山水画里
你从墨色深处被隐去"""

seg_list = jieba_seg(doc)
print("Default Mode:" + " ".join(seg_list))


model = gensim.models.Word2Vec.load('Chinese_Word2Vec/Word60.model')

for word in seg_list:
    # 换行符的特殊处理
    print("word:", word)
    if (word == '\n'):
        print('change line occur')
    try:
        print(model[word], '\n')
    except KeyError:
        pass

