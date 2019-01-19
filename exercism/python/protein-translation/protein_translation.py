def proteins(strand):
    result = list()
    def translator(cordon):
        if cordon == 'AUG':
            return 'Methionine'
        elif cordon in ['UUU', 'UUC']:
            return 'Phenylalanine'
        elif cordon in ['UUA', 'UUG']:
            return 'Leucine'
        elif cordon in ['UCU', 'UCC', 'UCA', 'UCG']:
            return 'Serine'
        elif cordon in ['UAU', 'UAC']:
            return 'Tyrosine'
        elif cordon in ['UGU', 'UGC']:
            return 'Cysteine'
        elif cordon == 'UGG' :
            return 'Tryptophan'
        elif cordon in ['UAA', 'UAG', 'UGA']:
            return 'Stop'

    for i in range(0, len(strand), 3):
        if i + 3 <= len(strand):
            translated = translator(strand[i : i + 3])
            if translated == 'Stop':
                break
            else:
                result.append(translated)

    return result