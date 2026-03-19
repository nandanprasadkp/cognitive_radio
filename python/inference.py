import numpy as np

def analyze_spectrum(model, signal_data, threshold=0.75):
    predictions = model.predict(signal_data, batch_size=64, verbose=0)
    results = []
    for i, pred in enumerate(predictions):
        conf = np.max(pred)
        idx = np.argmax(pred)
        status = "FREE" if conf < threshold else "BUSY"
        results.append({
            'id': i,
            'status': status,
            'modulation': MODS[idx] if status == "BUSY" else "Noise",
            'confidence': conf
        })
    return results