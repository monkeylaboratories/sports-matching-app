from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # スポーツ名
    sports_choice = (
        (1, '軟式野球'),
        (2, '硬式野球'),
        (3, 'サッカー'),
        (4, 'バスケットボール'),
    )
    sports = models.IntegerField(
        verbose_name='sports',
        choices=sports_choice,
        blank=True,
        null=True,
    )

    # 日時
    year_choice = (
        (2024, '2024年'),
        (2025, '2025年'),
        (2026, '2026年'),
    )
    month_choice = (
        (1, '1月'),
        (2, '2月'),
        (3, '3月'),
        (4, '4月'),
        (5, '5月'),
        (6, '6月'),
        (7, '7月'),
        (8, '8月'),
        (9, '9月'),
        (10, '10月'),
        (11, '11月'),
        (12, '12月'),
    )
    day_choice = [(i, f'{i}日') for i in range(1, 32)]

    hour_choice = [(i, f'{i}時') for i in range(0, 25)]

    min_choice = (
        (0, '0分'),
        (15, '15分'),
        (30, '30分'),
        (45, '45分'),
    )

    year = models.IntegerField(
        verbose_name='年',
        choices=year_choice,
        blank=True,
        null=True,
    )
    month = models.IntegerField(
        verbose_name='月',
        choices=month_choice,
        blank=True,
        null=True,
    )
    day = models.IntegerField(
        verbose_name='日',
        choices=day_choice,
        blank=True,
        null=True,
    )
    hour = models.IntegerField(
        verbose_name='時間',
        choices=hour_choice,
        blank=True,
        null=True,
    )
    min = models.IntegerField(
        verbose_name='分',
        choices=min_choice,
        blank=True,
        null=True,
    )

    # チーム名
    team = models.CharField(
        verbose_name='チーム名',
        max_length=20,
        blank=True,
        null=True,
    )

    # 試合場所
    location = models.CharField(
        verbose_name='試合場所',
        max_length=20,
        blank=True,
        null=True,
    )

    # チームレベル
    level = models.IntegerField(
        verbose_name='チームレベル',
        blank=True,
        null=True,
    )

    # サンプル項目2 一言
    memo = models.TextField(
        verbose_name='一言',
        blank=True,
        null=True,
    )

    """
    # サンプル項目1 文字列
    sample_1 = models.CharField(
        verbose_name='サンプル項目1 文字列',
        max_length=20,
        blank=True,
        null=True,
    )

    # サンプル項目2 メモ
    sample_2 = models.TextField(
        verbose_name='サンプル項目2 メモ',
        blank=True,
        null=True,
    )

    # サンプル項目3 整数
    sample_3 = models.IntegerField(
        verbose_name='サンプル項目3 整数',
        blank=True,
        null=True,
    )

    # サンプル項目4 浮動小数点
    sample_4 = models.FloatField(
        verbose_name='サンプル項目4 浮動小数点',
        blank=True,
        null=True,
    )

    # サンプル項目5 固定小数点
    sample_5 = models.DecimalField(
        verbose_name='サンプル項目5 固定小数点',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )

    # サンプル項目6 ブール値
    sample_6 = models.BooleanField(
        verbose_name='サンプル項目6 ブール値',
    )

    # サンプル項目7 日付
    sample_7 = models.DateField(
        verbose_name='サンプル項目7 日付',
        blank=True,
        null=True,
    )

    # サンプル項目8 日時
    sample_8 = models.DateTimeField(
        verbose_name='サンプル項目8 日時',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    sample_9_choice = (
        (1, '選択１'),
        (2, '選択２'),
        (3, '選択３'),
    )

    sample_9 = models.IntegerField(
        verbose_name='サンプル項目9_選択肢（固定）',
        choices=sample_9_choice,
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（マスタ連動）
    sample_10 = models.ForeignKey(
        User,
        verbose_name='サンプル項目10_選択肢（マスタ連動）',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    )
    """

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
