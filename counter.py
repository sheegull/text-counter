import re


def count_japanese_characters(file_path):
    """
    指定されたテキストファイル内の日本語の文字数をカウントします。

    :param file_path: 日本語の文字数をカウントするテキストファイルのパス
    :return: ファイル内の日本語の文字数
    """
    japanese_character_count = 0
    japanese_ranges = [
        (0x3000, 0x303F),  # ひらがな
        (0x3040, 0x309F),  # カタカナ
        (0x30A0, 0x30FF),  # 全角記号、カタカナ
        (0x4E00, 0x9FFF),  # 漢字
        (0xFF66, 0xFF9D),  # 半角カタカナ
    ]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                for char in line:
                    if any(
                        lower <= ord(char) <= upper for lower, upper in japanese_ranges
                    ):
                        japanese_character_count += 1
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

    return japanese_character_count


def count_english_and_digits(file_path):
    """
    指定されたテキストファイル内の英語と数字の文字数をカウントします。

    :param file_path: 英語と数字の文字数をカウントするテキストファイルのパス
    :return: ファイル内の英語と数字の文字数
    """
    english_and_digit_count = 0
    pattern = re.compile(r"[a-zA-Z0-9]")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                english_and_digit_count += len(pattern.findall(line))
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

    return english_and_digit_count


def count_total_characters(file_path):
    total_character_count = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                total_character_count += len(line)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

    return total_character_count


# 使用例
file_path = "sony_history.txt"  # カウントするファイルのパス
japanese_count = count_japanese_characters(file_path)
english_and_digit_count = count_english_and_digits(file_path)
total_count = count_total_characters(file_path)

print(f"ファイル '{file_path}' 内の日本語の文字数: {japanese_count}")
print(f"ファイル '{file_path}' 内の英語と数字の文字数: {english_and_digit_count}")
print(f"ファイル '{file_path}' 内の全文字数: {total_count}")
