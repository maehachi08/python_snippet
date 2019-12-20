# aws-pom

## python-fire について

* Class内にmethod定義すればサブコマンド
* Class内に private method定義すれば見えない
* Class内に property 定義すれば Value として利用可能
* helpメッセージに `--cluster_name` などの hyphen formatで表示したい場合
   * 第3引数以降に指定する

   ```
   def show(self, *, cluster_name: str):
       seld.cluster_name = cluster_name
   ```
