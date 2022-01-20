import xkcd_utilities


def main():
    comics_meta = xkcd_utilities.get_xckd_comics_meta(353)
    xkcd_utilities.save_xckd_pic_file(comics_meta)


if __name__ == '__main__':
    main()