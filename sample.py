# モジュールをロード
from jaxa.earth import je  # JAXA Earth API
import streamlit as st  # フレームワーク
from src.data_list import planet_images  # データベース的に使う
from src.create_img import create_planet_img  # 画像生成用

# カスタムCSSを使ってフッターを固定
footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: black;
    }
    </style>
    <div class="footer">
        <p>JAXA Earth API for Pythonのモジュールを利用しています</p>
    </div>
    """

# アプリケーション名
st.title("衛星画像アプリ")

# 画像データモデル一覧
options = planet_images
select_collection = st.selectbox(
    label="生成したい衛星画像", options=[index for index, option in options.items()]
)
select_band = st.selectbox(
    label="バンドID", options=[option for index, option in options.items()]
)

st.write("画像を取得する期間")

start_dlim = st.text_input(
    label="取得する日時", value="2018-01-01T00:00:00", placeholder="2018-01-01T00:00:00"
)

# 解像度入力
st.write("画像の解像度")
select_ppu = st.number_input(label="画像の解像度", value=100)

# 最小経度、緯度入力
st.write("最小経度・緯度")
min_col1, min_col2 = st.columns(2)
with min_col1:
    min_longitude = st.number_input(label="経度の最小値", value=120.00, step=0.01)
with min_col2:
    min_latitude = st.number_input(label="緯度の最小値", value=22.00, step=0.01)

# 最大経度、緯度入力
st.write("最大経度・緯度")
max_col1, max_col2 = st.columns(2)
with max_col1:
    max_longitude = st.number_input(label="経度の最大値", value=160.01, step=0.01)
with max_col2:
    max_latitude = st.number_input(label="緯度の最大値", value=55.01, step=0.01)

# Streamlitでボタンを押したときにgenerate関数を呼び出す
if st.button("衛星画像データ出力"):
    st.write(f"{start_dlim[:4]}年{start_dlim[5]}{start_dlim[6]}月頃の衛星写真")
    create_planet_img(
        select_collection,
        select_band,
        start_dlim,
        select_ppu,
        min_longitude,
        min_latitude,
        max_longitude,
        max_latitude,
    )

# フッターを追加
st.markdown(footer, unsafe_allow_html=True)
