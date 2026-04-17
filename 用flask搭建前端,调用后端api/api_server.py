import git
from flask import Flask, request, jsonify
from flask_cors import CORS
from test import call_llm

app = Flask(__name__)
CORS(app)


@app.route('/api/match', methods=['POST'])
def match_sentences():
    try:
        data = request.get_json()
        texts = data.get('texts', [])

        if not texts:
            return jsonify({'error': '请提供文本数据'}), 400

        results = []
        for text_pair in texts:
            if len(text_pair) != 2:
                return jsonify({'error': '每个文本对必须包含两个句子'}), 400

            result = call_llm([text_pair])
            results.append({
                'sentence1': text_pair[0],
                'sentence2': text_pair[1],
                'match_result': result
            })

        return jsonify({
            'success': True,
            'data': results
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
