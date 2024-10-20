import streamlit as st
from jaxa.earth import je
import matplotlib.pyplot as plt

def create_planet_img(
    collection, band, start, select_ppu, min_lon, min_lat, max_lon, max_lat
):
    # クエリパラメータを設定
    select_collection = collection
    select_band = band
    dlim = [start, start]
    ppu = select_ppu
    bbox = [min_lon, min_lat, max_lon, max_lat]

    # 画像を取得
    try:
        print("処理スタート")
        data = (
            je.ImageCollection(
                select_collection,
                ssl_verify=True,
            )
            .filter_date(dlim=dlim)
            .filter_resolution(ppu=ppu)
            .filter_bounds(bbox=bbox)
            .select(select_band)
            .get_images()
        )
        img = je.ImageProcess(data).show_images()
        st.pyplot(plt.gcf())  # StreamlitでMatplotlibのプロットを表示する

        return data  # 取得した画像データを返す
    
    except Exception as e:
        print("失敗してます")
        st.error(f"画像データの取得中にエラーが発生しました: {e}")
        return None  # エラーが発生した場合はNoneを返す