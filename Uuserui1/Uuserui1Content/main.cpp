#include "main.h"

class mainData : public QSharedData
{
public:
};

main::main(QObject *parent)
    : QObject{parent}
    , data(new mainData)
{}

main::main(const main &rhs)
    : data{rhs.data}
{}

main &main::operator=(const main &rhs)
{
    if (this != &rhs)
        data.operator=(rhs.data);
    return *this;
}

main::~main() {}
